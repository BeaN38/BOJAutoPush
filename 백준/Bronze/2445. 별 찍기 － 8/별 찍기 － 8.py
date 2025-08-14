star = int(input())

for i in range(1, star+1, 1):
    print("*"*i + " "*(star-i) + " "*(star-i) + "*"*i)

for i in range(star-1, 0, -1):
    print("*"*i + " "*(star-i) + " "*(star-i) + "*"*i)