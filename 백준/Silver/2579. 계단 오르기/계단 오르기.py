import sys
input = sys.stdin.readline

N = int(input())
dp = [0 for _ in range(301)]
score = [0 for _ in range(301)]

for i in range(N):
    score[i+1] = int(input())

dp[1] = score[1]
dp[2] = score[1] + score[2]

if N >= 3:
    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + score[i], dp[i-3] + score[i-1] + score[i])

print(dp[N])