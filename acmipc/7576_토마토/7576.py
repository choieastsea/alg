from sys import stdin
from collections import deque

input = stdin.readline

RIPED = 1
UNRIPED = 0
BLANK = -1

if __name__ =="__main__":
    m, n = map(int, input().split()) # 가로, 세로 크기(2~1000)
    tomato = [list(map(int, input().split())) for _ in range(n)]
    # 여러 지점에서 bfs를 시작한다. (i,j, day)를 넣어주면 될 듯
    q = deque()
    # 1. 시작 지점은 익은 토마토들
    targetCnt = 0
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            if tomato[i][j] == RIPED:
                q.append((i,j,0))
            elif tomato[i][j] == UNRIPED:
                targetCnt += 1
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    # 2. bfs로 0인 지점을 1로, day를 1씩 증가시키면서 탐색한다
    while len(q) > 0:
        # print(q)
        row, col, day = q.popleft()
        # 주변(4방향) 노드를 탐색하여 넣어줌
        for dr, dc in directions:
            next_row = row + dr
            next_col = col + dc
            if next_row >= 0 and next_row <=n-1 and next_col >=0 and next_col <=m-1 and tomato[next_row][next_col] == UNRIPED:
                tomato[next_row][next_col] = RIPED
                q.append((next_row, next_col, day + 1))
                targetCnt -= 1
    # for row in tomato:
    #     print(*row)
    if targetCnt == 0:
        print(day)
    else:
        print(-1)