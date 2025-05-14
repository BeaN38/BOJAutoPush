test_case = int(input()) # 테스트 케이스 입력

for i in range(test_case): # 테이스 케이스만큼 반복
    test_word = str(input())
    if i == 0:
        result = list(test_word) # 반복문 첫번째에서는 비교할 단어가 없으므로 result에 입력받은 단어 그대로 저장
    else:
        for j in range(len(test_word)): # 이후 result에 있는 단어와 비교하여 다를경우 ?로 변경
            if result[j] != test_word[j]:
                result[j] = "?"

for i in range(len(result)): # 정답 형식에 맞게 출력
    print(result[i], end="")