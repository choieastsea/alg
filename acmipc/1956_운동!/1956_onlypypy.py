from sys import stdin
input = stdin.readline
INF = float('inf')

v, e = map(int, input().split())  # v ~ 400
matrix = [[INF for _ in range(v)] for _ in range(v)]
for _ in range(e):
    strt, end, distance = map(int, input().split())
    matrix[strt-1][end-1] = distance
for via in range(v):
    # via 를 거쳐 가는게 더 빠르다면 업데이트
    for strt in range(v):
        if matrix[strt][via] == INF:
            continue
        for end in range(v):
            if matrix[strt][end] > matrix[strt][via] + matrix[via][end]:
                matrix[strt][end] = matrix[strt][via] + matrix[via][end]

min_cycle_distance = INF

for i in range(v):
    # cycle check and get minimum
    min_cycle_distance = min(min_cycle_distance, matrix[i][i])
print(min_cycle_distance if min_cycle_distance != INF else -1)
