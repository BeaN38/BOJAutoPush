import sys
from collections import deque
input = sys.stdin.readline

nodeCount = int(input()) # 노드의 갯수 입력
graph = [[] for _ in range(nodeCount+1)] # 간선 정보 저장용 그래프 생성
parent = [0 for _ in range(nodeCount+1)] # 부모 노드 저장용 리스트 생성
visited = [False for _ in range(nodeCount+1)] # 방문 여부 체크용 리스트 생성

for _ in range(nodeCount-1): # 간선 입력
    a, b = map(int, input().split())
    graph[a].append(b) # 입력 받은 간선 정보 저장
    graph[b].append(a) # 양방향 간선이므로 반대로도 저장

def bfs(start):
    queue = deque([start]) # 큐에 시작 노드 저장
    visited[start] = True # 시작 노드 방문 처리

    while queue: # 큐가 비어있지 않으면
        curr = queue.popleft() # 큐에서 값을 꺼내옴

        for next in graph[curr]: # 꺼내온 값과 연결된 노드 확인
            if not visited[next]: # 그 노드가 방문하지 않은 노드라면
                visited[next] = True # 방문 처리 후
                queue.append(next) # 큐에 집어넣음
                parent[next] = curr # 부모 정보 저장

bfs(1) # bfs 시행

for i in range(2, nodeCount+1): # 결과값 출력
    print(parent[i])