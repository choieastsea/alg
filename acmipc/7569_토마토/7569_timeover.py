from sys import stdin 
input = stdin.readline

RIPED = 1
SEMI_RIPED = 2
UNRIPED = 0
BLANK = -1

def countTomatos(tomato):
    """
    3차원 tomato에서 원소가 0인 갯수를 센다
    """
    unripedCnt = 0
    for square in tomato:
        for row in square:
            for el in row:
                if el == UNRIPED:
                    unripedCnt += 1
                # elif el == BLANK:
                #     blankCnt += 1
                
    return unripedCnt

def ripeAndGetCnt(tomato):
    """
    3차원 tomato에서 익힌 것 주변(최대6칸)만을 익힌다
    최대 100만 칸에서 일일이..? 시간초과나면 익힌것들 queue에 넣고 bfs 하면 될듯
    익힌 칸의 갯수를 리턴해보자!
    """
    cnt = 0
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            for k in range(len(tomato[i][j])):
                if tomato[i][j][k] == RIPED:
                    # 주변도 익히기, 하지만 같은 날에 해당 토마토의 주변도 익혀지지 않도록 해야함...
                    # print(i,j,k, tomato[i][j][k])
                    if i+1 <= h-1 and tomato[i+1][j][k] == UNRIPED:
                        cnt += 1
                        tomato[i+1][j][k] = SEMI_RIPED
                    if i-1 >= 0 and tomato[i-1][j][k] == UNRIPED:
                        cnt += 1
                        tomato[i-1][j][k] = SEMI_RIPED
                    if j+1 <= n-1 and tomato[i][j+1][k] == UNRIPED:
                        cnt += 1
                        tomato[i][j+1][k] = SEMI_RIPED
                    if j-1 >= 0 and tomato[i][j-1][k] == UNRIPED:
                        cnt += 1
                        tomato[i][j-1][k] = SEMI_RIPED
                    if k+1 <= m-1 and tomato[i][j][k+1] == UNRIPED:
                        cnt += 1
                        tomato[i][j][k+1] = SEMI_RIPED
                    if k-1 >= 0 and tomato[i][j][k-1] == UNRIPED:
                        cnt += 1
                        tomato[i][j][k-1] = SEMI_RIPED
    return cnt

def ripeComplete(tomato):
    """
    semiriped to ripe
    """
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            for k in range(len(tomato[i][j])):
                if tomato[i][j][k] == SEMI_RIPED:
                    tomato[i][j][k] = RIPED
                    

def printTomato(tomato):
    for i in range(len(tomato)):
        for j in range(len(tomato[i])):
            print(*tomato[i][j])
        print()

if __name__ == "__main__":
    m,n,h = map(int, input().split()) # 가로, 세로, 높이 -> 부피 100만 이하
    tomato = []
    for _ in range(h):
        # 정수 1은 익은 토마토, 정수 0 은 익지 않은 토마토, 정수 -1은 토마토가 들어있지 않은 칸
        tomato.append([list(map(int, input().split())) for _ in range(n)])
    # 익은 토마토 주위 6개 익히게 만듦
    day = 0
    unripedTomatos = countTomatos(tomato)
    while unripedTomatos != 0:
        # print(f'day {day}, 현재 {unripedTomatos}개 안익음')
        day += 1
        cnt = ripeAndGetCnt(tomato) # 익힌 토마토를 리턴
        ripeComplete(tomato) # semiriped -> riped
        # printTomato(tomato)
        # print(f'주변에 있던 {cnt}개 익힘')
        unripedTomatos -= cnt
        if cnt == 0:
            # 더 이상 익지 않음
            day = -1
            break
    print(day)