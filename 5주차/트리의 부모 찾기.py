import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

adj = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = list(map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)

check = [0 for _ in range(N+1)]
parent = [0 for _ in range(N+1)]

def bfs():
    q = deque([])
    q.appendleft(1)
    check[1] = 1

    while q:
        node = q.pop()
        for i in range(len(adj[node])):
            if not check[adj[node][i]]:
                q.appendleft(adj[node][i])
                check[adj[node][i]] = 1
                parent[adj[node][i]] = node

bfs()


for i in range(2, N+1):
    print(parent[i])
