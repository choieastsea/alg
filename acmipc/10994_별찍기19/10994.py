# https://www.acmicpc.net/problem/10994
def make_star_matrix(num):
    if num ==1:
        return [['*']]
    else:
        size = 4*num-3
        start = 0
        end = size - 1
        before_matrix = make_star_matrix(num-1)
        matrix = [[0 for j in range(size)] for i in range(size)]
        for row in range(size):
            for col in range(size):
                if row==start:
                    matrix[row][col] = '*'
                elif col==start:
                    matrix[row][col] = '*'
                elif row==end:
                    matrix[row][col] = '*'
                elif col==end:
                    matrix[row][col] = '*'
                # * 박고 빈칸 박아야함
                elif row == start + 1:
                    matrix[row][col] = ' '
                elif row == end - 1:
                    matrix[row][col] = ' '
                elif col == start + 1:
                    matrix[row][col] = ' '
                elif col == end - 1:
                    matrix[row][col] = ' '
                else:
                    matrix[row][col] = before_matrix[row-2][col-2]
        return matrix
    

def print_matrix(matrix):
    for line in matrix:
        for i in line:
            print(i,end="")
        print()

n = int(input())
matrix = make_star_matrix(n)
print_matrix(matrix)

# 해설
# 재귀
# basic case(n=1) : return [['*']]
# else :알맹이를 껍데기 두개로 둘러쌓아야함.
# 1번 껍데기 : *로 가득참
# 2번 껍데기 : 빈칸으로 가득참
# 알맹이 : n-1번째 실행 결과
