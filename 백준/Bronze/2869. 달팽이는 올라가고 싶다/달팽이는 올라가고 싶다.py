import sys # 빠른 입출력을 위한 sys 모듈 사용
import math # 올림 계산을 위한 math 모듈 사용용

A, B, V = map(int, sys.stdin.readline().split(' ')) # A, B, V 입력받음
day = 0 # 달팽이가 나무를 다 올라가는데 걸리는 일수

day = math.ceil((V - B) / (A - B)) # 올라가는데 걸리는 시간 = (전체 올라가야하는 높이 - 밤에 떨어지는 높이(마지막날은 밤이 없으므로)/(매일 올라가는 높이)

sys.stdout.write(str(day)) # 답 출력