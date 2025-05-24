from collections import deque # append와 pop의 시간복잡도를 O(N^N)에서 O(1)로 줄이기 위해 deque 모듈 사용

test_case = int(input()) # N값 입력받기
num_list = deque(range(1, test_case + 1)) # 1부터 N까지 리스트에 추가

while len(num_list) > 1: # 리스트의 길이가 1이 될때까지 반복
    num_list.popleft() # 맨 앞 제거
    num_list.append(num_list.popleft()) # 그 다음 숫자 뒤로 이동

print(num_list[0])