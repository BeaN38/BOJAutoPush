test_case = int(input()) # 테스트 케이스 입력
numList = [] # 입력받은 0이 아닌 수를 저장하는 리스트

for i in range(test_case): # 테이트 케이스만큼 반복
    Num = int(input()) # 숫자를 입력받은 후
    if Num != 0: # 0이 아니면 numList에 해당 숫자를 저장 
        numList.append(Num)
    else: # 0일경우, 가장 최근에 추가된 수를 리스트에서 제거 
        numList.pop()

print(sum(numList)) # 모든 계산이 끝난 후 답 출력