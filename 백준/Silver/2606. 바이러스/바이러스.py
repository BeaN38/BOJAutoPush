import sys

input = sys.stdin.readline

cpu = int(input())
connect_count = int(input())
result = 0

infect = [[] for _ in range(cpu+1)]

def dfs(num):
    visited_dfs[num] = True
    order_dfs.append(num)
    for nvnum in infect[num]:
        if not visited_dfs[nvnum]:
            dfs(nvnum)

for i in range(connect_count):
    a, b = map(int, input().split())
    infect[a].append(b)
    infect[b].append(a)

visited_dfs = [False] * (cpu+1)
order_dfs = []

dfs(1)

for i in visited_dfs:
    if i == True:
        result += 1

print(result-1)