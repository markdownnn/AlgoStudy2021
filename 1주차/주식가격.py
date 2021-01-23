def solution(prices):
    answer = []
    for i in range(len(prices)):
        if i == len(prices) - 1:
            answer.append(0)
            break
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                break
            if j == len(prices) - 1:
                answer.append(j - i)
    return answer