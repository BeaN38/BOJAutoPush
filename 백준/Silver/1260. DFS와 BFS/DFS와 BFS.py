import sys
from collections import deque
input = sys.stdin.readline

def dfs(v):
    visited.append(v)
    print(v, end=' ')

    for i in graphs[v-1]:
        if visited.count(i) == 0:
            dfs(i)

def bfs(v):
    visited.append(v)
    bfs_deque.append(v)

    while bfs_deque:
        nodeCurr = bfs_deque.popleft()
        print(nodeCurr, end=' ')

        for i in graphs[nodeCurr-1]:
            if visited.count(i) == 0:
                bfs_deque.append(i)
                visited.append(i)


nodeCount, lineCount, nodeStart = map(int, input().split())
visited = []
graphs = [[] for _ in range(nodeCount)]
bfs_deque = deque()

for i in range(lineCount):
    a, b = map(int, input().split())
    graphs[a-1].append(b)
    graphs[b-1].append(a)

for j in range(nodeCount):
    graphs[j].sort()

dfs(nodeStart)
visited = []
print()
bfs(nodeStart)