from sys import stdin
input = stdin.readline

def multiple(a,b, n, m, k):
    """
    a,b를 행렬곱 연산 수행
    a : n*m
    b : m*k
    결과 : n*k
    """
    matrix = [[0 for _ in range(k)]for _ in range(n)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            element = 0
            for x in range(m):
                element += a[i][x] * b[x][j]
            matrix[i][j] = element
    return matrix

def printMat(matrix):
    for row in matrix:
        print(*row)

if __name__ == "__main__":
    n, m = map(int, input().split()) # A: n*m matrix
    a = []
    for _ in range(n):
        row = list(map(int, input().split()))
        a.append(row)
    m, k = map(int, input().split()) # B: m*k matrix
    b = []
    for _ in range(m):
        row = list(map(int, input().split()))
        b.append(row)
    mat = multiple(a,b, n,m,k)
    printMat(mat)