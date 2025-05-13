import math
import sys

test_case = int(sys.stdin.readline().rstrip())
num_list = []
total = 0
averageNum = 0 # 산술평균
centerNum = 0 # 중앙값
centerIndex = (test_case + 1) // 2 - 1
modeNum = 0 # 최빈값
rangeNum = 0 # 범위
count_dict = {}
max_mode_list = []

for i in range(test_case):
    num = int(sys.stdin.readline().rstrip())
    total += num
    num_list.append(num)

num_list.sort()

averageNum = round(total / test_case)
centerNum = num_list[centerIndex]
rangeNum = num_list[-1] - num_list[0]

for i in num_list:
    if i in count_dict:
        count_dict[i] += 1
    else:
        count_dict[i] = 1

max_mode = max(count_dict.values())

for num in count_dict:
    if count_dict[num] == max_mode:
        max_mode_list.append(num)

max_mode_list.sort()

if len(max_mode_list) == 1:
    modeNum = max_mode_list[0]
else:
    modeNum = max_mode_list[1]


sys.stdout.write(str(averageNum) + "\n")
sys.stdout.write(str(centerNum) + "\n")
sys.stdout.write(str(modeNum) + "\n")
sys.stdout.write(str(rangeNum) + "\n")