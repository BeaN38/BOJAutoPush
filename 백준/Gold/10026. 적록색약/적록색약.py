import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
graph = [] # 색 체크용 2차원 리스트
bfs_deque = deque()
visit = [[False for _ in range(N)] for _ in range(N)] # 방문 체크용 2차원 리스트
result = 0

for _ in range(N): # 색 입력받아서 그래프에 저장
    graph.append(list(map(str, input().strip())))

for a in range(N): # 모든 칸에 대해서 방문하지 않았으면 결과값 + 1 후 bfs 탐색 시행
    for b in range(N):
        if visit[b][a] == False:
            result += 1
            visit[b][a] = True # bfs 탐색을 시작하면서 시작점 방문 표시
            bfs_deque.append((a, b)) # bfs 덱에 탐색 시작할 위치 넣고 bfs 탐색 시작
        while bfs_deque: # 더이상 탐색할 곳이 없을때까지 반복
            x, y = bfs_deque.popleft() # 덱에서 위치값을 꺼내고
            color = graph[y][x] # 색 확인
            for i in range(4): # 상하좌우 체크
                cx = x + dx[i]
                cy = y + dy[i]

                if 0 <= cy < N and 0 <= cx < N: # 인덱스 범위를 초과하지 않았는지 확인
                    if visit[cy][cx] == False and graph[cy][cx] == color: # 방문하지 않았고, 색이 같으면 그 위치도 bfs 탐색
                        bfs_deque.append((cx, cy))
                        visit[cy][cx] = True # 방문 표시

print(result, end=' ') # 첫번째 답 출력

for i in range(N): # 모든 칸에 대해 방문 기록 초기화 후, 초록색 칸을 빨간색으로 변환
    for j in range(N):
        visit[j][i] = False
        if graph[j][i] == 'G':
            graph[j][i] = 'R'

result = 0 # 결과값 초기화

for a in range(N): # 이전과 똑같이 모든칸에 대해 bfs 탐색 시행
    for b in range(N):
        if visit[b][a] == False:
            result += 1
            visit[b][a] = True
            bfs_deque.append((a, b))
        while bfs_deque:
            x, y = bfs_deque.popleft()
            color = graph[y][x]
            for i in range(4):
                cx = x + dx[i]
                cy = y + dy[i]

                if 0 <= cy < N and 0 <= cx < N:
                    if visit[cy][cx] == False and graph[cy][cx] == color:
                        bfs_deque.append((cx, cy))
                        visit[cy][cx] = True

print(result) # 두번째 답 출력