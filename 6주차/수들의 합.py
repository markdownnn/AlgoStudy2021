import sys

input = sys.stdin.readline

N, M = list(map(int, input().split()))
num = list(map(int, input().split()))

s, e = 0, 0

result, answer = 0, 0

while True:
    if result < M:
        if e == N:
            break
        result += num[e]
        e += 1
    else:
        if result == M:
            answer += 1
        result -= num[s]
        s += 1

print(answer)
        
