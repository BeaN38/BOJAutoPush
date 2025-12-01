import sys
input = sys.stdin.readline

N = int(input())
result = 0
row_list = [0 for _ in range(N)] # N 크기만큼 0으로 채운 빈 배열 생성

def check(row): # 대각선 or 같은 열에 Queen이 존재하는지 체크. 존재한다면 False 반환. 존재하지 않으면 True 반환.
    for i in range(row):
        if row_list[row] == row_list[i] or abs(row_list[row] - row_list[i]) == abs(row - i):
            return False
    return True

def dfs(row): # dfs 탐색. 0번 인덱스부터 Queen을 넣어봄. check로 다른 Queen과 충돌하지 않는 경우만 이어서 진행.
    if row == N: # 마지막 위치까지 문제 없이 다 들어갈 경우 결과값에 +1 추가
        global result
        result += 1
        return
    
    for i in range(N):
        row_list[row] = i

        if check(row):
            dfs(row + 1)

dfs(0) # 0번 인덱스부터 탐색 시작

print(result) # 정답 출력