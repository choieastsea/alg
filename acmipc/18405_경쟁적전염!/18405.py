from sys import stdin
input = stdin.readline
from collections import deque

def solution(second,x,y):
    """
    s초 뒤의 x,y의 바이러스 번호를 리턴
    """
    global numLocationList
    global q
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    if second > 0: # 0초일때는 감염을 진행하지 않는다!
        while len(q) > 0:
            num, r, c, s = q.popleft()
            # print(num,r,c,s)
            # 주변 0이라면 n으로 감염
            # q에다가 1부터 넣어놨고 level을 s로 표현했으니 한 레벨당 모든 숫자를 차례대로 돌 것이다!!
            for drow, dcol in directions:
                next_row = r + drow
                next_col = c + dcol
                # print('next row & col :',next_row,next_col)
                if next_row >= 0 and next_row <= n-1 and next_col >= 0 and next_col <= n-1 and matrix[next_row][next_col] == 0:
                    matrix[next_row][next_col] = num
                    if s < second-1:
                        # second초 일때, queue가 비도록 하기 위해
                        q.append((num,next_row,next_col,s+1))
                        # print(num,next_row,next_col,s+1,'추가됨')
    # print()
    # for row in matrix:
    #     print(*row)
    # print()
    return matrix[x-1][y-1]

def initLocation(matrix):
    """
    초기 matrix에서, bfs를 위한 초기 queue를 리턴
    이때, 1부터 k까지 순서대로 (숫자, row, col, 0)을 넣어준다. 0은 0초를 의미
    """
    global k
    numLocation = [[]for _ in range(k+1)] # numLocation[k] : k가 있는 위치 (row,col)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] != 0:
                numLocation[matrix[i][j]].append((i,j))
    q = deque()
    for i, locations in enumerate(numLocation):
        for row, col in locations:
            q.append((i,row,col,0)) # number, row, col, second
    return q

if __name__ == "__main__":
    n, k = map(int, input().split()) # n*n & k 종류(1~)의 바이러스 번호
    matrix = [list(map(int, input().split()))for _ in range(n)]
    q = initLocation(matrix) # for bfs
    s, x, y = map(int, input().split()) 
    print(solution(s,x,y))

    