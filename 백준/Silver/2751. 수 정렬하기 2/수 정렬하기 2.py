import sys # 빠른 입출력을 위해 sys 모듈을 불러옴 

test_case = int(sys.stdin.readline()) # 테스트 케이스 N 입력
numList = [] # 숫자들을 담을 리스트 선언

for i in range(test_case): # N만큼 반복
    Num = int(sys.stdin.readline()) # 수를 입력받으면 리스트에 저장
    numList.append(Num)

numList.sort() # 모든 수가 저장된 후 오름차순으로 정렬

for i in range(len(numList)): # 정렬된 리스트 값 출력 
    sys.stdout.write(str(numList[i]) + "\n")