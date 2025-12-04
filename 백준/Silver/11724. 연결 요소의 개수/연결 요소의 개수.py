import sys
from collections import deque
input = sys.stdin.readline

nodeCount, M = map(int, input().split())
graph = [[] for _ in range(nodeCount + 1)]
visit = [False for _ in range(nodeCount + 1)]
bfs_deque = deque()
result = 0

def bfs(start):
    bfs_deque.append(start)
    visit[start] = True

    while bfs_deque:
        now = bfs_deque.popleft()
        for i in graph[now]:
            if not visit[i]:
                visit[i] = True
                bfs_deque.append(i)

for _ in range(M):
    nodeStart, nodeEnd = map(int, input().split())
    graph[nodeStart].append(nodeEnd)
    graph[nodeEnd].append(nodeStart)

for i in range(1, nodeCount+1):
    if not visit[i]:
        result += 1
        bfs(i)

print(result)