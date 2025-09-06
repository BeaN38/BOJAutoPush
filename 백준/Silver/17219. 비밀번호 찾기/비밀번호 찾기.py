import sys

input = sys.stdin.readline

Pw, needPw = map(int, input().split())
pw_dict = {}

for _ in range(Pw):
    site, password = input().split()
    pw_dict[site] = password

for _ in range(needPw):
    site = input().strip()
    print(pw_dict[site])