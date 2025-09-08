import sys
input = sys.stdin.readline

n = int(input())

dp = [0] * (n+2)
dp[0] = 1
dp[1] = 1

def dpp(n):
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp

if n >= 2:
    dpp(n)

print(dp[n]%10007)