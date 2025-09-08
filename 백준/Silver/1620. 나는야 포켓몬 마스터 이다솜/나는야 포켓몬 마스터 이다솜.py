import sys
input = sys.stdin.readline

all_num, needSearch = map(int, input().split())
name_list = []

for i in range(all_num):
    name_list.append(input().strip())

for i in range(needSearch):
    data = input().strip()

    if data.isdigit():
        print(name_list[(int(data)-1)])
    else:
        print((name_list.index(data)) + 1)