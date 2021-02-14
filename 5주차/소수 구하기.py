import sys
from math import sqrt

M, N = list(map(int, sys.stdin.readline().split()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

for i in range(M, N+1):
    if is_prime(i):
        print(i)
