import sys
input = sys.stdin.readline

if __name__ == '__main__':
    n, k = map(int, input().split(' '))
    S = [[0 for _ in range(n+1)] for _ in range(n+1)] # S[i][j] : A[0][0]부터 A[i][j]까지의 합 
    for i in range(n):
        line = list(map(int, input().split(' ')))
        line_S = [0 for _ in range(n+1)]
        for j in range(n):
            line_S[j+1] = line_S[j] + line[j]
            S[i+1][j+1] = S[i][j+1] + line_S[j] + line[j]
    # print('S',S)
    for _ in range(k):
        row1, col1, row2, col2 = map(int, input().split(' '))
        sec1 = S[row2][col2]
        sec2 = S[row1-1][col2]
        sec3 = S[row2][col1-1]
        sec4 = S[row1-1][col1-1]
        print(sec1 - sec2 - sec3 + sec4)
        