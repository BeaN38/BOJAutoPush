N = int(input())
result = 0
num = 0

list_time = list(map(int, input().split()))

list_time.sort()

for i in range(N):
    for j in range(0, i+1, 1):
        num += list_time[j]
    result += num
    num = 0

print(result)