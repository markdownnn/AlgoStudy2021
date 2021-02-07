import sys

N = int(sys.stdin.readline()) # 이걸 이용해서 입력을 받음
M = int(sys.stdin.readline())
broken = sys.stdin.readline().split()

now = 100
closest, move = -1, 0
only_move = abs(now - N)

while True:
    if N - move >= 0: # 반례 찾기가 어려움. -1이 먼저 와야 한다.
        for i in range(len(broken)):
            if broken[i] in str(N-move):
                break
        else:
            closest = N-move
            break
    for i in range(len(broken)):
        if broken[i] in str(N+move):
            break
    else:
        closest = int(N+move)
        break
    move += 1
    if move >= only_move:
        break

move += len(str(closest))

print(min(move, only_move))