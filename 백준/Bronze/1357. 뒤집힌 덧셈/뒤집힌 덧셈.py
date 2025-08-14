a, b = map(int, input().split())

rev_a = int(str(a)[::-1])
rev_b = int(str(b)[::-1])

rev_result = rev_a + rev_b

print(int(str(rev_result)[::-1]))