import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

bfs_deque = deque()
x, y, z = map(int, input().split())
graph = []
result = 0

for _ in range(z): # 3차원 배열 입력
    floor = []
    for _ in range(y):
        floor.append(list(map(int, input().split())))

    graph.append(floor)

for a in range(z): # 모든 칸을 탐색하여 1이 있으면 bfs 덱에 저장
    for b in range(y):
        for c in range(x):
            if graph[a][b][c] == 1:
                bfs_deque.append((c, b, a))

while bfs_deque: # bfs 탐색이 끝날때까지 반복
    nx, ny, nz = bfs_deque.popleft()
    for n in range(6): # 6방향 확인
        cx = nx + dx[n]
        cy = ny + dy[n]
        cz = nz + dz[n]

        if 0 <= cx < x and 0 <= cy < y and 0 <= cz < z: # 인덱스 범위를 벗어나지 않고
            if graph[cz][cy][cx] == 0: # 덜익은 토마토가 있으면
                graph[cz][cy][cx] = (graph[nz][ny][nx] + 1) # 익는데 걸리는 시간 +1로 값 변경(시작값이 1이므로)
                bfs_deque.append((cx, cy, cz)) # 덱에 그 토마토 위치 저장

for a in range(z): # 모든 칸을 탐색하여 익는데 걸리는 최장시간 확인
    for b in range(y):
        for c in range(x):
            if graph[a][b][c] > result + 1:
                result = graph[a][b][c] - 1
            if graph[a][b][c] == 0: # 만약 덜익은 토마토가 남아있으면 -1 출력
                print(-1)
                exit(0)

print(result)