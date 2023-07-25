import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def searchAdj(matrix, i, j):
    """ 
    배추 위치에서 실행되는 함수
    해당 배추를 방문처리하고 주변을 탐색
    """
    if matrix[i][j] == 1:
        matrix[i][j] = 2 # 방문안한 배추라면, 방문 처리
        height = len(matrix)
        width = len(matrix[0])
        if i < height - 1 and matrix[i+1][j] == 1: # 배추인 경우만 탐색
            searchAdj(matrix, i+1, j)
        if j < width - 1 and matrix[i][j+1] == 1:
            searchAdj(matrix, i, j+1)
        if i >= 1 and matrix[i-1][j] == 1:
            searchAdj(matrix, i-1, j)
        if j >= 1 and matrix[i][j-1] == 1:
            searchAdj(matrix, i, j-1)

def solution(matrix):
    """
    k 개의 배추가 matrix 밭에 위치할 때,
    인접 그룹의 수
    """
    group_cnt = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                searchAdj(matrix, i, j) # 방문하지 않은 배추와 그 인접한 배추들을 모두 방문처리한다
                group_cnt += 1
    return group_cnt

if __name__ =="__main__":
    case = int(input())
    for _ in range(case):
        width, height, k = map(int, input().split()) # 가로, 세로, 배추 갯수
        matrix = [[0 for _ in range(width)]for __ in range(height)] # 0 : 아무것도 아님, 1 : 배추, 2: 방문한 배추
        for __ in range(k):
            y,x = map(int, input().split())
            matrix[x][y] = 1
        answer = solution(matrix)
        print(answer)