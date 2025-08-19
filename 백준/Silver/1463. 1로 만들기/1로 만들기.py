import sys

num = int(sys.stdin.readline().strip())
dp = [0] * (num + 1)
dp[1] = 0

for i in range(2, num+1):
    dp[i] = dp[i-1] + 1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

sys.stdout.write(str(dp[num]))

# dp? : 동적 계획법. 큰 계산을 작은 계산으로 쪼개고, 이미 계산한 결과를 저장해서 필요할 때 재사용하는 방법
# 예를 들어, dp[4]는 -1연산시 dp[3] + 1 = 1 + 1 = <2>이고 /2연산시 dp[2] + 1 = 1 + 1 = <2>이므로
# min(2, 2) = 2. 따라서 dp[4] = 2