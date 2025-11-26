import sys
from collections import deque
input = sys.stdin.readline

test_case = int(input())


for i in range(test_case):
    docCount, docFind = map(int, input().split())
    doc_deque = deque(map(int, input().split()))
    count = 0
    while True:
        if doc_deque[0] < max(doc_deque):
            doc = doc_deque.popleft()
            doc_deque.append(doc)
            if docFind == 0:
                docFind = len(doc_deque) - 1
            else:
                docFind -= 1
        else:
            doc = doc_deque.popleft()
            count += 1
            if docFind == 0:
                print(count)
                break
            else:
                docFind -= 1