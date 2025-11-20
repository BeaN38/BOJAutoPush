import sys
input = sys.stdin.readline

test_case = int(input())
list_time = list(map(int, input().split()))
list_time.sort()

result = 0
now_total_time = 0
for i in range(test_case):
    result += now_total_time + list_time[i]
    now_total_time += list_time[i]

print(result)