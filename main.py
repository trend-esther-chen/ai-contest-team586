import argparse
import logging
from datetime import datetime

import pandas as pd
from dotenv import load_dotenv
from langchain.callbacks import get_openai_callback
from tqdm import tqdm

from utils.common_utils import (extract_folder_and_name_from_path,
                                read_files_from_directory,
                                update_estimate_used_cost_file)
from utils.log import logger
from utils.question_solver import QuestionSolver

# Load .env file
load_dotenv()

# Usage
question_folder, question_filename = extract_folder_and_name_from_path(
    "Question_FILE", "./questions/question.txt"
)
solution_folder, solution_filename = extract_folder_and_name_from_path(
    "Solution_FILE", "./solutions/solution.py"
)

parser = argparse.ArgumentParser(
    description="A script that accepts a question path and a solution save path"
)
parser.add_argument(
    "--question-path",
    default=question_folder,
    help="The path to the questions (folder)",
)
parser.add_argument(
    "--solution-save-path",
    default=solution_folder,
    help="The path to save the solution",
)
parser.add_argument("--debug", action="store_true", help="Set log level to DEBUG")
args = parser.parse_args()

if args.debug:
    logger.setLevel(logging.DEBUG)
    for handler in logger.handlers:
        handler.setLevel(logging.DEBUG)

if __name__ == "__main__":
    # Initialize an empty DataFrame with the columns 'Question file', 'code' and 'ChatGPT_thought'
    df = pd.DataFrame(columns=["Question file", "Solution code", "ChatGPT thought"])
    try:
        questions = read_files_from_directory(args.question_path)
        if len(questions) > 1:
            logger.warning(
                "According to the requirements of the competition server, we anticipate that there should only be"
                " one question.txt present, which is root/questions/question.txt, but now we've detected multiple!"
            )

        for q in tqdm(questions):
            solver = QuestionSolver()
            # If you want to estimate the cost please include the call to chatgpt in the following context manager
            with get_openai_callback() as cb:
                result = solver.solve(q[1])
            update_estimate_used_cost_file(cb.prompt_tokens, cb.completion_tokens)

            logger.debug(f"Prompt Tokens: {cb.prompt_tokens}")
            logger.debug(f"Completion Tokens: {cb.completion_tokens}")
            logger.debug("result:\n" + str(result))

            chatgpt_thought = result["thought"]
            solution_code = result["solution_code"]
            new_row = pd.DataFrame(
                {
                    "Question file": [q[0]],
                    "Solution code": [solution_code],
                    "ChatGPT thought": [chatgpt_thought],
                }
            )

            df = pd.concat([df, new_row], ignore_index=True)

        # Get current timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Save DataFrame to CSV
        solution_detail_save_path = f"{args.solution_save_path}/{timestamp}.csv"
        df.to_csv(solution_detail_save_path, index=False)
        logger.info(f"Solution detail have been saved to {solution_detail_save_path}")

        solution_save_path = f"{args.solution_save_path}/{solution_filename}"
        with open(solution_save_path, "w") as f:
            f.write(df.loc[0, "Solution code"])
            logger.info(f"Solution file have been saved to {solution_save_path}")
            if len(questions) > 1:
                logger.warning(
                    "The competition server expects us to handle one question at a time, "
                    "but now we have received multiple answers because there are multiple txt files "
                    f"under the ./questions folder. However, we will only save question from {questions[0][0]}"
                    " as solutions/solution.py and it will be scored by the competition server."
                )

    except Exception as e:
        logger.error(f"Exception:\n {str(e)} happened!", exc_info=True)
