import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

test_case = int(input())

for i in range(test_case): # 테스트 케이스만큼 반복
    result = 0 # 결과값 초기화
    bfs_deque = deque() # bfs 덱 초기화
    x, y, k = map(int, input().split()) # x, y, k 값 입력
    graph = [[0] * x for _ in range(y)] # x * y 사이즈만큼 0으로 채워진 2차원 배열 생성

    for j in range(k): # k 만큼 배추 위치 입력
        nx, ny = map(int, input().split())
        graph[ny][nx] = 1
    
    for a in range(x): # 모든 x, y 방문
        for b in range(y):
            if graph[b][a] == 1: # 배추가 심어져 있으면
                graph[b][a] = 0 # 일단 배추를 지우고
                bfs_deque.append((a, b)) # 배추 위치를 bfs 덱에 추가
                result += 1 # 애벌레 수 +1
                while bfs_deque: # bfs 덱이 비워질때까지 테스트
                    nx, ny = bfs_deque.popleft() # 지금 테스트할 배추 위치값을 덱에서 꺼냄
                    for n in range(4): # 상하좌우 확인
                        cx = nx + dx[n]
                        cy = ny + dy[n]

                        if 0 <= cx < x and 0 <= cy < y: # 리스트 범위를 벗어나지 않고
                            if graph[cy][cx] == 1: # 인접한 곳에 또 배추가 있으면
                                graph[cy][cx] = 0 # 그 배추도 지움
                                bfs_deque.append((cx, cy)) # 그 배추 위치도 bfs에 저장
    
    print(result)