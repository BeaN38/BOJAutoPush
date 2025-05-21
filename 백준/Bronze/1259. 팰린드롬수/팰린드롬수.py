while True: # 0을 입력받을때까지 무한 반복
    num = list(input()) # 숫자를 입력받으면 1자리씩 잘라서 리스트에 저장
    if num == ['0']: # 0을 입력받았다면 작동 종료
        break
    result = "yes" # 기본값은 yes
    for i in range(len(num) // 2): # 양끝 인덱스를 비교하므로 전체 비교횟수는 숫자 길이 // 2
        if num[i] != num[-(i + 1)]: # 양끝 인덱스가 다르면 result = no
            result = "no"
            break
    print(result) # 답 출력