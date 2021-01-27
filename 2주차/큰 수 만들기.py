def solution(number, k):
    start_idx = 0
    while k:
        k -= 1
        del_idx = len(number) - 1
        if start_idx == -1:
            start_idx = 0
        for i in range(start_idx, len(number) - 1):
            if number[i] < number[i+1]:
                del_idx = i
                start_idx = i - 1
                break
        if del_idx == len(number) - 1:
            return number[:len(number)-k-1]
        number = number[:del_idx]+number[del_idx+1:]
    return number