import sys
input = sys.stdin.readline

length = int(input())
CurrNumList = 1
stack = []
result = []
NO = False

for i in range(length):
    NeedNum = int(input())
    while True:
        if len(stack) == 0:
            stack.append(CurrNumList)
            result.append("+")
            CurrNumList += 1
        elif stack[-1] == NeedNum:
            stack.pop()
            result.append("-")
            break
        else:
            stack.append(CurrNumList)
            result.append("+")
            CurrNumList += 1
            if NeedNum < stack[-1]:
                NO = True
                break

if NO == False:
    for i in range(len(result)):
        print(result[i])
else:
    print("NO")