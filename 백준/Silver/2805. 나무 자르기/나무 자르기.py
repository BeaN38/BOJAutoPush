import sys
input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

start = 0 # 이분 탐색 시작 = 0
end = max(tree) # 이분 탐색 끝 = 가장 긴 나무 길이
result = 0

while start <= end: # 시작값이 끝값보다 커질때까지(이분 탐색이 끝날때까지)반복
    mid = (start + end) // 2 # 중앙값을 시작값과 끝값의 중간으로 업데이트
    total = 0 # 잘린 나무 길이의 합 초기화
    for i in range(N): # 모든 나무에 대해 절단기보다 클 경우, total에 잘린 길이 합산
        if tree[i] > mid:
            total += (tree[i] - mid)
    if total >= M: # 잘린 길이 >= M이면 result을 mid로 갱신하고 시작값을 방금 테스트한 값 + 1로 변경
        result = mid
        start = mid + 1
    else: # 잘린 길이 < M이면 끝값을 방금 테스트한 값 - 1로 변경
        end = mid - 1

print(result) # 답 출력