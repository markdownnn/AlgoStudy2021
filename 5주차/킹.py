import sys

input = sys.stdin.readline

board = [[0 for _ in range(8)] for _ in range(8)]

k, s, n = input().split()

n = int(n)

k_r, k_c = 8-int(k[1]), ord(k[0])-ord('A')
s_r, s_c = 8-int(s[1]), ord(s[0])-ord('A')

orders = []

for i in range(n):
    orders.append(input().rstrip())

move = {"R":[0, 1],
        "L":[0, -1],
        "B":[1, 0],
        "T":[-1, 0],
        "RT":[-1, 1],
        "LT":[-1, -1],
        "RB":[1, 1],
        "LB":[1, -1]}

for i in range(n):
    move_r, move_c = move[orders[i]]
    new_r, new_c = k_r + move_r, k_c + move_c
    if new_r >= 0 and new_r < 8 and new_c >= 0 and new_c < 8:
        if new_r == s_r and new_c == s_c:
            if s_r + move_r >= 0 and s_r + move_r < 8 and s_c + move_c >= 0 and s_c + move_c < 8:
                k_r = new_r
                k_c = new_c
                s_r += move_r
                s_c += move_c
        else:
            k_r = new_r
            k_c = new_c

        
print(str(chr(ord('A')+k_c)+str(8-k_r)))
print(str(chr(ord('A')+s_c)+str(8-s_r)))
