import sys
input = sys.stdin.readline

n = int(input())
A = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j, el in enumerate(row):
        A[j][i] = el
# A는 n개의 n-sized sorted list로 구성되어 있음!
# print(A)
# 여기서 n번째로 큰 것을 찾자(merge sort랑 약간 비슷한 느낌으로)
for i in range(n):
    max_value = 0
    max_index = 0
    for j in range(n):
        if max_value <= A[j][-1]:
            max_value = A[j][-1]
            max_index = j
    answer = A[max_index].pop()
print(answer)

## 메모리 초과 나므로, PQ의 size를 제한하는 방법으로 구현하기 ...