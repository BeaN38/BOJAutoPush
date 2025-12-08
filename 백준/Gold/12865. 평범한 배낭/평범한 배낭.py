import sys
input = sys.stdin.readline

items, limit = map(int, input().split())
dp = [[0 for _ in range(limit+1)] for _ in range(items+1)]
itemList = [[0, 0]]

for i in range(items):
    itemList.append(list(map(int, input().split())))

for i in range(1, items+1, 1):
    weight = itemList[i][0]
    value = itemList[i][1]

    for j in range(1, limit+1, 1):
        if j < weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight] + value)

print(dp[items][limit])