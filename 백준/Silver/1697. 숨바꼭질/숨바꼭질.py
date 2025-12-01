import sys
from collections import deque
input = sys.stdin.readline

start, target = map(int, input().split())

bfs_deque = deque()
bfs_deque.append(start)
visit = [0 for _ in range(100001)] # 방문 여부 체크 & 방문까지 소요시간 체크용 배열

if start == target: # 만약 이미 목표지점에 있다면 0 출력 후 종료
    print(0)
    exit(0)

while visit[target] == 0: # 목표 지점에 방문할때까지 반복
    curr = bfs_deque.popleft() # 덱에 있는 값을 꺼내서

    if curr - 1 >= 0 and visit[curr - 1] == 0: # -1 위치에 도달하지 않았으면 -1 방문 체크, 소요시간 추가, 덱에 값 추가
        visit[curr - 1] = visit[curr] + 1
        bfs_deque.append(curr - 1)

    if curr + 1 <= 100000 and visit[curr + 1] == 0: # +1 위치에 도달하지 않았으면 +1 방문 체크, 소요시간 추가, 덱에 값 추가
        visit[curr + 1] = visit[curr] + 1
        bfs_deque.append(curr + 1)

    if curr * 2 <= 100000 and visit[curr * 2] == 0: # *2 위치에 도달하지 않았으면 *2 방문 체크, 소요시간 추가, 덱에 값 추가
        visit[curr * 2] = visit[curr] + 1
        bfs_deque.append(curr * 2)

print(visit[target]) # 결과 출력