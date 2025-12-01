import sys
input = sys.stdin.readline

N, M = map(int, input().split())
s = []

def dfs():
    if len(s) == M: # M길이 도달시 출력
        print(' '.join(map(str, s)))
        return
    
    for i in range(1, N+1): # 모든 N에 대해 반복
        if i not in s: # i가 s에 없으면
            s.append(i) # i를 s에 넣은 후
            dfs() # dfs 호출 -> 다음 dfs 함수가 이어서 값을 넣음
            s.pop() # 호출한 dfs가 모든 경우의 수를 출력하면 맨 뒤 값을 제거함

dfs()