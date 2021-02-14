import sys

n = int(sys.stdin.readline())
series = list(map(int, sys.stdin.readline().split()))

dp = [0 for i in range(n)]

dp[0] = series[0]

for i in range(1, n):
    dp[i] = max(series[i], dp[i-1]+series[i])

print(max(dp))
