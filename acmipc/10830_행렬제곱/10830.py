from sys import stdin
input = stdin.readline
C = 1000

def squareMatrix(matrix):
    size = len(matrix)
    resultMatrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            element = 0
            for k in range(size):
                element += matrix[i][k] * matrix[k][j]
            resultMatrix[i][j] = element % C
    # print(f'matrix : {matrix}, after pow :{resultMatrix}')
    return resultMatrix

def multiplyMatrix(m1, m2):
    size = len(m1)
    resultMatrix = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            element = 0
            for k in range(size):
                element += m1[i][k] * m2[k][j]
            resultMatrix[i][j] = element % C
    # print(f'{m1} * {m2} = {resultMatrix}')
    return resultMatrix

def rest(A, C):
    """
    A의 각 원소를 C로 나눈 나머지로 업데이트함
    """
    for i in range(len(A)):
        for j in range(len(A)):
            A[i][j] %= C
    return A

def powMatrix(A,B):
    """
    A 행렬을 B 거듭제곱하고 각 원소를 1000으로 나눈 나머지를 결과로 리턴
    """
    # print(f'powMatrix({A},{B})')
    if B == 1:
        return rest(A,C) # 1000으로 나눈 나머지여야할텐데!! 여기서 틀린 것 같음
    if B % 2 == 0:
        return squareMatrix(powMatrix(A,B//2))
    else:
        return multiplyMatrix(squareMatrix(powMatrix(A,B//2)),A)

if __name__ == "__main__":
    N, B = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(list(map(int, input().split())))
    result = powMatrix(A,B)
    for row in result:
        print(*row)
