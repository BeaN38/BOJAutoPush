import sys
import heapq
input = sys.stdin.readline

needInput = int(input())
heap = []

for _ in range(needInput):
    num = int(input())
    if num == 0:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)