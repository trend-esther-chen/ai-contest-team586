def solution(N):
    binary = bin(N)[2:]
    max_gap = 0
    current_gap = 0
    start_counting = False

    for digit in binary:
        if digit == '1':
            if start_counting:
                max_gap = max(max_gap, current_gap)
                current_gap = 0
            else:
                start_counting = True
        elif start_counting:
            current_gap += 1

    return max_gap