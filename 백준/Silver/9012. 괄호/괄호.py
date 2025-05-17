test_case = int(input()) # 테스트케이스 입력

for i in range(test_case): # 테스트케이스만큼 반복
    isVPS = "YES"
    text = str(input()) # 문자열을 입력받은 후
    testList = []
    for j in range(len(text)):
        if text[j] == "(": # 괄호가 열리면 리스트에 괄호 추가
            testList.append(text[j])
        else: # 괄호가 닫히면 리스트에서 괄호를 제거. 만약 제거할 괄호가 없으면 isVPN = NO
            if len(testList) == 0:
                isVPS = "NO"
                break
            else:
                testList.pop()
    if len(testList) != 0: # 만약 괄호 검사가 끝났는데도 리스트에 괄호가 남아있다면 isVPN = NO
        isVPS = "NO"
    print(isVPS) # 결과값 출력