import sys

from collections import deque

input = sys.stdin.readline

N, K = list(map(int, input().split()))

name = [[] for i in range(21)]

for i in range(N):
    data = input().rstrip()
    name[len(data)].append(i)

answer = 0

for i in range(21):
    if name[i]:
        q = deque([ name[i][0] ])
        for j in range(1, len(name[i])):
            while q and q[0] < name[i][j] - K:
                q.popleft()
            answer += len(q)
            q.append(name[i][j])
        

print(answer)
