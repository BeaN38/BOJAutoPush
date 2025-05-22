while True: # 무한반복
    sides = list(map(int, input().split())) 
    if sides == [0, 0, 0]: # 입력으로 0 0 0을 받으면 반복 종료
        break
    sides.sort() # 입력받은 후 크기순으로 나열 (큰값이 빗변)
    if sides[0]**2 + sides[1]**2 == sides[2]**2: # 피타고라스 계산
        print("right")
    else:
        print("wrong")
