test_case = int(input())
num_list = list(map(int, input().split()))

sosu = 0 # 소수 갯수
result = 0 # 나눠떨어진 횟수

for i in range(len(num_list)):
    result = 0
    num = num_list[i]
    for j in range(1, num+1):
        if num % j == 0:
            result += 1
        if j == num:
            if result == 2:
                sosu += 1

print(sosu)