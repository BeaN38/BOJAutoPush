import sys
input = sys.stdin.readline

while True:
    a, b = map(int, input().split())
    if not (a == 0 and b == 0):
        print(a+b)
    else:
        break