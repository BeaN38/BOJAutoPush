import sys
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)] # index와 value가 동일한 배열 생성(size = n+1)

def union(a, b): # 집합을 합치는 함수: 각 인덱스의 부모가 같은지 확인하고 다를경우 동일하게 맞춤.
    rootA = find(a)
    rootB = find(b)

    if rootA != rootB:
        parent[rootB] = rootA

def find(x): # 부모를 찾는 함수
    if parent[x] == x: # 부모가 자기 자신이면 자기 자신 반환
        return x
    
    parent[x] = find(parent[x]) # 아닐경우, 부모값을 따라올라가며 부모값을 갱신하고, 최종 값을 찾으면 그 값을 반환
    return parent[x]

for i in range(m): # m만큼 반복
    command, a, b = map(int, input().split())
    if command == 0: # command가 0이면 집합을 합침
        union(a, b)
    else: # command가 1이면 각 인덱스의 부모값을 찾고 같으면 yes 다르면 no 출력
        if find(a) == find(b):
            print("yes")
        else:
            print("no")