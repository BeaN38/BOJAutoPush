import sys
input = sys.stdin.readline

N = int(input())
cost = [[0] * 3 for _ in range(1000)] # 입력으로 들어오는 촤대 크기의 2차원 배열 생성
dp = [[0] * 3 for _ in range(1000)] # 입력으로 들어오는 최대 크기의 2차원 배열 생성

for i in range(N): # 2차원 배열에 각 집 위치의 색칠 비용 값 추가
    r, g, b = map(int, input().split())
    cost[i][0] = r
    cost[i][1] = g
    cost[i][2] = b

# 첫번째 인덱스는 인덱스 에러를 막기 위해 미리 채워둠(아래 반복문에서 i-1에 접근하므로)
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N): # 어떤 색을 칠하는지에 따라 이전에 다른 색을 칠한 비용값에 현재 비용값을 더함
    dp[i][0] = min(dp[i-1][1] + cost[i][0], dp[i-1][2] + cost[i][0])
    dp[i][1] = min(dp[i-1][0] + cost[i][1], dp[i-1][2] + cost[i][1])
    dp[i][2] = min(dp[i-1][0] + cost[i][2], dp[i-1][1] + cost[i][2])

print(min(dp[N-1][0], dp[N-1][1], dp[N-1][2])) # 마지막 인덱스에서 가장 비용이 적은 값 출력