import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

bfs_deque = deque()
x, y = map(int, input().split())
graph = []
result = 0

for i in range(y): # 토마토 정보 입력
    graph.append(list(map(int, input().split())))

for a in range(x): # 모든 칸에 대해서 익은 토마토의 위치를 덱에 넣음
    for b in range(y):
        if graph[b][a] == 1:
            bfs_deque.append((a, b))

while bfs_deque: # bfs 탐색이 끝날때까지 반복
    nx, ny = bfs_deque.popleft() # 덱에서 위치값을 가져와서
    for n in range(4): # 상하좌우 확인
        cx = nx + dx[n]
        cy = ny + dy[n]

        if 0 <= cx < x and 0 <= cy < y: # 배열의 인덱스 범위를 초과하지 않고
            if graph[cy][cx] == 0: # 덜익은 토마토가 있다면
                graph[cy][cx] = (graph[ny][nx] + 1) # 익는데 걸리는 시간 +1로 값 변경(시작이 0이 아닌 1이므로)
                bfs_deque.append((cx, cy)) # 그리고 그 위치도 덱에 저장

for i in range(x): # bfs 계산이 끝난 후 모든 칸 탐색
    for j in range(y):
        if graph[j][i] > result + 1: # 익는데 걸리는 최장시간 값을 result에 저장(아까 +1 했으니 여기서 -1)
            result = graph[j][i] - 1
        if graph[j][i] == 0: # 아직 익지 않은 토마토가 존재한다면 탐색 중지. -1 출력
            print(-1)
            exit(0) # 답을 출력했으므로 종료시킴

print(result)