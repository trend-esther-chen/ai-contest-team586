#!/bin/bash
set -a; . .env 

# evalmessage: Information on the execution result of the previous run of solution.py by the game server.
# Contestants should consider how to utilize this information themselves.

evalmessage="${1:-""}"
evalmessage_cleaned=$(echo -n "$evalmessage" | tr -d '[:space:]\\r\\n\\t')

if [ -z "$evalmessage_cleaned" ]; then
  # first round
  killall -9 python >/dev/null 2>&1
  mkdir -p solutions
  rm -rf solutions/* # This depends on your approach
fi

python main.py