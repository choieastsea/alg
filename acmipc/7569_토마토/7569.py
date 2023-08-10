from sys import stdin
from collections import deque
input = stdin.readline

RIPED = 1
UNRIPED = 0
BLANK = -1

if __name__ == "__main__":
    m, n, h = map(int, input().split())  # 가로, 세로, 높이 -> 부피 100만 이하
    tomato = []
    for _ in range(h):
        # 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
        tomato.append([list(map(int, input().split())) for _ in range(n)])
    
    targetCnt = h*m*n # 여기서 빈칸 갯수 뺀만큼이 목표치
    curRipedCnt = 0 # 현재 익은 토마토 수

    q = deque()  # for bfs
    day = 0
    riped_location = []
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == RIPED:
                    riped_location.append((i, j, k))
                    q.append(((i, j, k), day))
                    curRipedCnt += 1
                elif tomato[i][j][k] == BLANK:
                    targetCnt -= 1
    if targetCnt == 0:
        print(0)
        exit(0)
    # 익은 토마토 주위 6개 익히게 만듦 -> BFS 여러 출발지점을 두도록 함
    while len(q) > 0:
        curLocation, curDate = q.popleft()
        # print(curLocation, curDate)
        i, j, k = curLocation
        # 주변 익히기
        if i+1 <= h-1 and tomato[i+1][j][k] == UNRIPED:
            curRipedCnt += 1
            tomato[i+1][j][k] = RIPED
            q.append(((i+1, j, k), curDate+1))

        if i-1 >= 0 and tomato[i-1][j][k] == UNRIPED:
            curRipedCnt += 1
            tomato[i-1][j][k] = RIPED
            q.append(((i-1, j, k), curDate+1))

        if j+1 <= n-1 and tomato[i][j+1][k] == UNRIPED:
            curRipedCnt += 1
            tomato[i][j+1][k] = RIPED
            q.append(((i, j+1, k), curDate+1))

        if j-1 >= 0 and tomato[i][j-1][k] == UNRIPED:
            curRipedCnt += 1
            tomato[i][j-1][k] = RIPED
            q.append(((i, j-1, k), curDate+1))

        if k+1 <= m-1 and tomato[i][j][k+1] == UNRIPED:
            curRipedCnt += 1
            tomato[i][j][k+1] = RIPED
            q.append(((i, j, k+1), curDate+1))

        if k-1 >= 0 and tomato[i][j][k-1] == UNRIPED:
            curRipedCnt += 1
            tomato[i][j][k-1] = RIPED
            q.append(((i, j, k-1), curDate+1))

    # print()
    # for i in range(len(tomato)):
    #     for j in range(len(tomato[i])):
    #         print(*tomato[i][j])
    #     print()
    # print(curRipedCnt, targetCnt)

    # 다 했는데도 안 익은게 있다면 -1 출력
    if curRipedCnt < targetCnt:
        print(-1)
    else:
        print(curDate) # maxDate으로 갱신하지 않아도됨(후진 없으므로 마지막 curDate이 가장 마지막 날짜 의미)
