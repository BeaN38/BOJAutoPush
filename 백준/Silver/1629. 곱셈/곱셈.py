import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
print(pow(A, B, C)) # pow(a, b, c) = a**b (mod c)를 빠르게 계산하는 내장 함수