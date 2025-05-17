import sys # 빠른 입출력을 위해 sys 모듈 사용
from collections import Counter # 시간 초과 문제를 해결하기 위해 빠르게 값을 찾아주는 Counter모듈 사용

N = int(sys.stdin.readline()) # N값 입력
numArrayList = [] # 카드에 적힌 숫자들을 담을 리스트
countArrayList = [] # 카드의 갯수를 구할 숫자들을 담을 리스트
result = [] # 카드가 몇장 있는지 결과를 담을 리스트

numArrayList = list(map(int, sys.stdin.readline().split())) # 카드에 적힌 숫자를 입력받고 리스트에 저장

M = int(sys.stdin.readline()) # M값 입력

countArrayList = list(map(int, sys.stdin.readline().split())) # 갯수를 구할 숫자를 입력받고 리스트에 저장
counter = Counter(numArrayList)

for i in range(M): # M만큼 반복
    result.append(counter[countArrayList[i]]) # 갯수를 구한 후 결과값에 저장

for i in range(len(result) - 1):
    sys.stdout.write(str(result[i]) + " ") # 출력 형식에 맞게 출력
sys.stdout.write(str(result[-1]))