import sys

from collections import deque

read = sys.stdin.readline

N, M = list(map(int, read().split()))

board = [[0 for _ in range(M)] for _ in range(N)]
check1 = [[0 for _ in range(M)] for _ in range(N)]
check2 = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = read()
    for j in range(M):
        board[i][j] = int(row[j])

move = [[-1,0],[1,0],[0,-1],[0,1]]

def bfs():
    q = deque([])
    q.append((0,0,0, True))
    check1[0][0] = 1
    check2[0][0] = 1
    while q:
        r, c, depth, can_break = q.popleft()
        if r == N - 1 and c == M - 1:
            print(depth + 1)
            break
        for i in range(4):
            new_r, new_c = r + move[i][0], c + move[i][1]
            if new_r >= 0 and new_r < N and new_c >= 0 and new_c < M:
                if not board[new_r][new_c]:
                    if not check1[new_r][new_c] and can_break:
                        q.append((new_r, new_c, depth+1, can_break))
                        check1[new_r][new_c] = 1
                        check2[new_r][new_c] = 1
                    elif not check2[new_r][new_c] and not can_break:
                        q.append((new_r, new_c, depth+1, can_break))
                        check2[new_r][new_c] = 1
                else:
                    if not check2[new_r][new_c] and can_break:
                        q.append((new_r, new_c, depth+1, False))
                        check2[new_r][new_c] = 1
    else:
        print(-1)

bfs()
