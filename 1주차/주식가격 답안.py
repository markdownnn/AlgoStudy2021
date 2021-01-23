from collections import deque # 이거 쓸 필요 없음
def solution(prices):
    answer = []
    prices = deque(prices)
    while prices:
        c = prices.popleft() # pop(0)로 대체 가능

        count = 0
        for i in prices:
            if c > i:
                count += 1
                break
            count += 1

        answer.append(count)

    return answer