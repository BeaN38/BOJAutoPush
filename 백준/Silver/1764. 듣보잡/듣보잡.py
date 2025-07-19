n, m = map(int, input().split())
word_list = set()
result = []

for i in range(n):
    word_list.add(str(input()).strip())

for j in range(m):
    word = str(input().strip())
    if word in word_list:
        result.append(word)
        
result.sort()

print(len(result))
for k in range(len(result)):
    print(result[k])