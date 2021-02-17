import sys

N, M = list(map(int, sys.stdin.readline().split()))

adj = [[] for i in range(N)]

for i in range(M):
    fr1, fr2 = list(map(int, sys.stdin.readline().split()))
    adj[fr1].append(fr2)
    adj[fr2].append(fr1)

visited = [False for i in range(N)]

def dfs(v, depth):
    global ans
    visited[v] = True
    if depth >= 4:
        ans = True
        return
    for nxt in adj[v]:
        if not visited[nxt]:
            dfs(nxt, depth+1)
            visited[nxt] = False

ans = False
for i in range(N):
    dfs(i, 0)
    visited[i] = False
    if ans:
        break

print(1 if ans else 0)
