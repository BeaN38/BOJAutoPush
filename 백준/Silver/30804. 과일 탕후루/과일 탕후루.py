import sys
input = sys.stdin.readline

n = int(input())
numList = list(map(int, input().split())) # 입력으로 받는 과일 리스트
fruitList = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # 과일의 갯수를 저장할 리스트
kind = 0 # 현재 과일 종류 수
left = 0 # 리스트의 가장 왼쪽 끝 인덱스
maxConnect = 0 # 연결된 과일의 최대 길이

for right in range(n): # 입력으로 받은 과일 리스트의 맨 처음부터 끝까지 반복
    if fruitList[numList[right]] == 0: # 만약 없는 과일이면
        kind += 1 # 종류 추가
    fruitList[numList[right]] += 1 # 과일 갯수 추가
    
    while kind > 2: # 2종류를 넘어가면 2종류가 될때까지 왼쪽을 1칸씩 지움
        a = numList[left]
        fruitList[a] -= 1
        if fruitList[a] == 0:
            kind -= 1
        left += 1

    current_len = right - left + 1 # 현재 길이가 이전 최대길이보다 길면 최대 길이 갱신
    if maxConnect < current_len:
        maxConnect = current_len

print(maxConnect) # 답 출력