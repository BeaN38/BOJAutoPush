import sys
input = sys.stdin.readline

test_case = int(input())
numList = [1, 1, 1, 2, 2] + [0] * 100

def result(num):
    a = 5
    while a <= num:
        numList[a] = numList[a-1] + numList[a-5]
        a += 1
    return numList[num]

for _ in range(test_case):
    num = int(input())
    print(result(num-1))