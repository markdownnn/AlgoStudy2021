def solution(numbers, target, current=0):
    if len(numbers) == current:
        if target == 0:
            return 1
        else:
            return 0
    return solution(numbers, target-numbers[current], current+1) + solution(numbers, target+numbers[current], current+1)