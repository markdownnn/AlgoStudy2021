import sys    

N, M, D = map(int, sys.stdin.readline().split())

board = []

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def get_distance(self, other):
        return abs(self.x-other.x)+abs(self.y-other.y)
    def move(self):
        self.y += 1

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

enemy = []

for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            enemy.append(Point(j, i))

from itertools import combinations
import copy # copy.deepcopy()로 깊은 복사

archor_combination = list(combinations([i for i in range(M)], 3)) # 인자로 리스트와 선택하는 수 전달

answer = 0

for combination in archor_combination:
    archor = []
    e = copy.deepcopy(enemy)
    can_take_down = len(e)
    for idx in combination:
        archor.append(Point(idx, N))
    while e:
        shortest_list = []
        for i in range(len(archor)):
            shortest, shortest_idx = D, -1
            left = M - 1
            for j in range(len(e)):
                if archor[i].get_distance(e[j]) <= shortest:
                    if archor[i].get_distance(e[j]) == shortest:
                        if e[j].x <= left:
                            left = e[j].x
                            shortest = archor[i].get_distance(e[j])
                            shortest_idx = j
                    else:
                        left = e[j].x
                        shortest = archor[i].get_distance(e[j])
                        shortest_idx = j
            if shortest_idx != -1:
                shortest_list.append(shortest_idx)
        e = [e[i] for i in range(len(e)) if i not in shortest_list]
        passed = []
        for i in range(len(e)):
            e[i].move()
            if e[i].y >= N:
               passed.append(i)
        e = [e[i] for i in range(len(e)) if i not in passed]
        can_take_down -= len(passed)
    answer = max(answer, can_take_down)

print(answer)