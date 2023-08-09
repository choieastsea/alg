from sys import stdin
from copy import deepcopy
input = stdin.readline

BLANK = 0
WALL = 1
VIRUS = 2

def expandVirus(row, col):
    """
    row, col이 virus일 때, 상하좌우 주변이 blank라면 virus로 업데이트
    """
    global matrix
    global n
    global m
    
    # basic case
    matrix[row][col] = VIRUS
    # recursion case
    if row-1 >= 0 and matrix[row-1][col] == BLANK:
        expandVirus(row-1, col) # 상
    if row+1 <= n-1 and matrix[row+1][col] == BLANK:
        expandVirus(row+1, col) # 하
    if col-1 >= 0 and matrix[row][col-1] == BLANK:
        expandVirus(row, col-1) # 좌
    if col+1 <= m-1 and matrix[row][col+1] == BLANK:
        expandVirus(row, col+1) # 우

def getSafeArea(matrix):
    """
    virus는 주변 모든 blank로 퍼져나감
    이때, 남은 blank의 수가 안전영역의 크기
    """
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == VIRUS:
                expandVirus(i,j) # matrix update
    safeArea = 0
    for row in matrix:
        # print(*row)
        for el in row:
            if el == BLANK:
                safeArea += 1
    # print(f'safeArea : {safeArea}')
    return safeArea

if __name__ =="__main__":
    n,m = map(int, input().split()) # 세로 크기 n, 가로 m // 3 ≤ N, M ≤ 8
    original_matrix = [list(map(int, input().split())) for _ in range(n)]
    matrix = deepcopy(original_matrix)
    # 3개의 벽을 배치... 0의 갯수 combination 3 개의 경우의 수가 존재하는데...
    maxSafeArea = 0
    for i in range(n*m):
        # i => [i//n][i%n]
        # print(f'{i}){matrix[i//n][i%n]}')
        if matrix[i // m][i % m] == BLANK:
            for j in range(i+1, n*m):
                if matrix[j // m][j % m] == BLANK:
                    for k in range(j+1, n*m):
                    # i, j, k에 벽을 배치 한 후 safeArea를 구해서 min 값을 구함
                        if matrix[k // m][k % m] == BLANK:
                            matrix[i // m][i % m] = WALL
                            matrix[j // m][j % m] = WALL
                            matrix[k // m][k % m] = WALL
                            # print('i,j,k:',i,j,k)
                            # print(f'[{i//n}][{i%n}] / [{j//n}][{j%n}] / [{k//n}][{k%n}]를 벽으로')
                            # print(f'{matrix[i // n][i % n]}, {matrix[j // n][j % n]}, {matrix[k // n][k % n]}')
                            maxSafeArea = max(maxSafeArea, getSafeArea(matrix))
                            matrix = deepcopy(original_matrix) # 원본으로 되돌려서 다음 경우의 수
    print(maxSafeArea)
