N, K = map(int, input().split(' ')) # N, K를 입력받음
result_list = [] # 답을 저장할 리스트
removed_list = [] # 중복되는 수를 막기 위해 값을 지워나갈 리스트
count = 0
target = 0

# 리스트에 1부터 N까지 수를 담음
for i in range(1, (N+1)):
    removed_list.append(i)

# 필요한 인덱스 값을 반환하는 함수
def NextIndex(Num, K):
    length = len(removed_list)
    result = Num-1
    result += K
    if result >= length:
        while True:
            result -= length
            if result < length:
                break
    return result

# 값을 모두 채워넣을때까지 반복
while count != N:
    target = NextIndex(target, K)
    result_list.append(removed_list[target])
    removed_list.remove(removed_list[target])
    count += 1

# 출력 형식에 맞게 출력
print("<", end="")
for i in range(N-1):
    print(result_list[i], end=", ")
print(result_list[-1], end=">")