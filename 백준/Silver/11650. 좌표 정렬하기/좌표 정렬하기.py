test_case = int(input()) # 테스트 케이스 입력
xy = [] # 좌표 저장 리스트 생성

for i in range(test_case): # 테스트 케이스만큼 좌표를 입력받아서 xy 리스트에 저장
    xy.append(list(map(int, input().split())))

xy.sort() # 파이썬에서 2차원 배열을 sort하면 첫번째 인자의 크기를 비교한 후, 두번쨰 인자의 크기를 비교하여 정렬함

for i in range(test_case): # 답 출력
    print(str(xy[i][0]) + " " + str(xy[i][1]))
