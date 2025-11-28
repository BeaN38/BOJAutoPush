import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

y, x = map(int, input().split())
graph = []
bfs_deque = deque() # bfs 검사용 덱 생성
bfs_deque.append((0, 0)) # 시작위치값(0, 0) 저장

for i in range(y): # 입력받은 미로를 2차원 배열로 저장
    row = list(map(int, input().strip()))
    graph.append(row)

while graph[-1][-1] == 1: # 마지막 칸을 검사할때까지 반복
    cy, cx = bfs_deque.popleft() # bfs에 저장된 '검사해야할 위치값'을 꺼내서
    for i in range(4): # 상하좌우 체크
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx >= 0 and ny >= 0 and nx < x and ny < y: # x, y 인덱스 초과 확인
            if graph[ny][nx] == 1: # 인덱스 초과하지 않고, 그 다음칸이 길(1)이면
                bfs_deque.append((ny, nx)) # bfs에 그 칸 추가하고
                graph[ny][nx] += graph[(ny - dy[i])][(nx - dx[i])] # 이전 칸까지 지나온 칸수를 더함

print(graph[-1][-1])