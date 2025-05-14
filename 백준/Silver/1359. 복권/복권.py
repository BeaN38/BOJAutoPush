import math

RangeNum, SelectNum, PassNum = map(int, input().split()) # 총 숫자 범위, 선택할 갯수, 당첨 기준
result = 0

for i in range(PassNum, SelectNum+1):  # 적어도 PassNum개의 숫자를 맞출 확률을 구해야 하므로 PassNum부터 SelectNum까지 값을 올리며 모든 확률을 합산함
    CombinationAll = math.comb(RangeNum, SelectNum) # N개의 숫자 범위중 R개를 뽑는 경우의 수
    CombinationSelected = math.comb(SelectNum, i) # 선택할 갯수중 당첨되는 번호들을 뽑는 경우의 수
    CombinationSelectedX = math.comb(RangeNum - SelectNum, SelectNum - i) # N-선택할 갯수중 당첨이 아닌 번호들을 뽑는 경우의 수
    result += (CombinationSelected * CombinationSelectedX) / CombinationAll

print(result)
