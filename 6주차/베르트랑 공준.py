import sys
from math import sqrt, floor

input = sys.stdin.readline

memo = [-1 for i in range(300000)]
memo[1] = False
memo[2] = True


def is_prime(n):
    if memo[n] != -1:
        return memo[n]
    if n % 2 == 0:
        return False
    for i in range(3, floor(sqrt(n))+1, 2):
        if n % i == 0:
            memo[n] = False
            return False
    memo[n] = True
    return True

while True:
    n = int(input())
    result = 0
    if not n:
        break
    for i in range(n+1, 2*n+1):
        result += is_prime(i)
    print(result)
