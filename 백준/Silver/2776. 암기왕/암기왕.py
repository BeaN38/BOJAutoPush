import sys

input = sys.stdin.readline

test_case = int(input())

for _ in range(test_case):
    note1Count = int(input())
    note1 = {x: True for x in map(int, input().split())}
    note2Count = int(input())
    note2 = list(map(int, input().split()))

    for i in range(note2Count):
        if note2[i] in note1:
            print(1)
        else:
            print(0)