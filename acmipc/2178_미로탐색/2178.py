import sys
from collections import deque
"""
최단거리는 BFS로 푸는 것이 합리적임
최단거리에 대한 값을 queue에 넣어주면서 탐색을 하는데, 주의해야할 점으로는
1. queue에 주변 노드를 넣을 때 방문 처리와 거리 둘다 넣도록
2. 처음 방문한 곳이 항상 최단거리임을 보장하도록(되돌아가지 않도록)
3. 범위 체크
"""
input = sys.stdin.readline

AVAILABLE = 1 # but not visited
VISITED = 2


if __name__ == "__main__":
    n, m = map(int, input().split()) # 2<= n, m <= 100
    matrix = [] # 0 : 불가, 1 : 가능하지만 방문하지 않음, 2 : 방문
    for _ in range(n):
        row = list(map(int, list(input().strip())))
        matrix.append(row)

    q = deque()
    q.append((0,0,1)) # entry point (row, col, distance)
    matrix[0][0] = VISITED

    while len(q) > 0:
        # print(q)
        row, col, distance = q.popleft()
        if row == n-1 and col == m-1:
            #basic case
            print(distance)
            exit(0)
        if row + 1 < n and matrix[row + 1][col] == AVAILABLE:
            q.append((row+1,col,distance+1))
            matrix[row + 1][col] = VISITED
        if col + 1 < m and matrix[row][col+1] == AVAILABLE:
            q.append((row,col+1,distance+1))
            matrix[row][col + 1] = VISITED
        if row - 1 >= 0 and matrix[row - 1][col] == AVAILABLE:
            q.append((row-1,col,distance+1))
            matrix[row - 1][col] = VISITED
        if col - 1 >= 0 and matrix[row][col-1] == AVAILABLE:
            q.append((row,col-1,distance+1))
            matrix[row][col - 1] = VISITED
