import sys

input = sys.stdin.readline

N, K = list(map(int, input().split()))
A = list(map(int, input().split()))

robot = []
robot_arr = [0 for i in range(2*N)]

up, down = 0, N-1

def move():
    global up
    global down
    up -= 1
    down -= 1
    if up < 0:
        up = 2*N - 1
    if down < 0:
        down = 2*N - 1
    for i in range(len(robot)):
        if robot[i] == down:
            robot_arr[down] = 0
            robot.pop(i)
            break

def check_robot(index):
    for i in range(len(robot)):
        if robot[i] == index:
            return True
    return False

def robot_move():
    for i in range(len(robot)):
        move_to = robot[i] + 1 if robot[i] + 1 <= 2 * N - 1 else 0
        if A[move_to] >= 1 and not robot_arr[move_to]:
            robot_arr[robot[i]] = 0
            robot_arr[move_to] = 1
            robot[i] = move_to
            A[move_to] -= 1
    for i in range(len(robot)):
        if robot[i] == down:
            robot_arr[down] = 0
            robot.pop(i)
            break

def place_robot():
    global up
    if A[up] >= 1 and not robot_arr[up]:
        robot.append(up)
        A[up] -= 1
        robot_arr[up] = 1

def check_K():
    num_K = 0
    for i in range(len(A)):
        if A[i] == 0:
            num_K += 1
    if num_K >= K:
        return True
    return False

count = 0

while True:
    count += 1
    move()
    robot_move()
    place_robot()
    if check_K():
        break

print(count)