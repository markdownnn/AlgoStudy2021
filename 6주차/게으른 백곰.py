import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))

ice = [0 for i in range(1000001)]

result, answer = 0, 0

for i in range(N):
    g, x = list(map(int, input().split()))
    ice[x] = g

for position in range(len(ice)):
    if position > K * 2:
        result -= ice[position-K*2-1]
    result += ice[position]
    answer = max(answer, result)

print(answer)
