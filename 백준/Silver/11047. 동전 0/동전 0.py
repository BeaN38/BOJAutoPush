N, K = map(int, input().split())
list_coin = []
result = 0

for i in range(N):
    list_coin.append(int(input()))

while K != 0:
    for i in range(N-1, -1, -1):
        if list_coin[i] <= K:
            a = K // list_coin[i]
            K = K % list_coin[i]
            result += a
            break

print(result)