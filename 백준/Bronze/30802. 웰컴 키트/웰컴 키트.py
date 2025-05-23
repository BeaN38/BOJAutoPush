import math

N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

group_t = 0
for i in range(6):
    group_t += math.ceil(sizes[i] / T)
print(group_t)

total_p = N // P
remain_p = N % P
print(total_p, remain_p)