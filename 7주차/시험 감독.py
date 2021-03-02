import sys
from math import ceil

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = list(map(int, input().split()))

result = len(A)

for i in range(len(A)):
    A[i] -= B
    if A[i] > 0:
        result += ceil(A[i] / C)

print(result)