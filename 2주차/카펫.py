def solution(brown, yellow):
    total_length = (brown - 4) / 2
    i = 1
    while(i <= total_length - i):
        if i * (total_length - i) == yellow:
            return [total_length-i+2, i+2]
        i += 1