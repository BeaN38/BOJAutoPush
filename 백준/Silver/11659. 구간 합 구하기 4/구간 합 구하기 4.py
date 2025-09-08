import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numList = [0] + list(map(int, input().split()))
totalSum = [0] * (n+1)

def total_sum(n):
    totalSum[0] = numList[0]
    for i in range(1, n+1):
        totalSum[i] = totalSum[i-1] + numList[i]
    return totalSum

total_sum(n)

for _ in range(m):
    total = 0
    a, b = map(int, input().split())
    total = totalSum[b] - totalSum[a-1]
    print(total)