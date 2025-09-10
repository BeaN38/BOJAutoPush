import sys
input = sys.stdin.readline

coins, price = map(int, input().split())

if coins*100 >= price:
    print("Yes")
else:
    print("No")