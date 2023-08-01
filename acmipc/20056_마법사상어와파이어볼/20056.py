from sys import stdin
input = stdin.readline

def getMoveCount(direction, speed):
    if direction == 0:
        return (-speed, 0)
    elif direction == 1:
        return (-speed,speed)
    elif direction == 2:
        return (0,speed)
    elif direction == 3:
        return (speed,speed)
    elif direction == 4:
        return (speed,0)
    elif direction == 5:
        return (speed,-speed)
    elif direction == 6:
        return (0,-speed)
    elif direction == 7:
        return (-speed,-speed)
    else:
        print('direction error')
        exit(-1)

def getLocationAfterMove(before, d, n):
    after = before + d
    while after < 0:
        after += n
    if after > n-1:
        after %= n
    return after

class FireBall:
    def __init__(self, row, col, mass, speed, direction) -> None:
        self.row = row
        self.col = col
        self.mass = mass
        self.speed = speed
        self.direction = direction

    def move(self, n):
        """
        n sized matrix에서 이동 시킴(row, col)
        """
        drow, dcol = getMoveCount(self.direction, self.speed)
        self.row = getLocationAfterMove(self.row, drow, n)
        self.col = getLocationAfterMove(self.col, dcol, n)
        return self.row, self.col
    
    def __str__(self) -> str:
        return f'({self.mass}, {self.speed}, {self.direction})'
        # return f'{self.mass}'
        

def moveFireball(matrix, fireballList):
    """
    모든 파이어볼의 위치를 direction방향으로 speed만큼 이동시킨다
    matrix에 파이어볼 추가
    벗어난 경우, 1~N 행/열은 연결되어있음에 유의
    """
    for fireball in fireballList:
        row, col = fireball.move(n)
        matrix[row][col].append(fireball)

def makeFourFireball(row,col,sumMass, sumSpeed, directionSet, fireBallCnt):
    """
    모인 파이어볼로 4개를 만든다
    """
    mass = int(sumMass/5)
    speed = int(sumSpeed/fireBallCnt)
    if mass > 0:
        if len(directionSet) == 1: # 모두 짝수나 홀수
            # 0,2,4,6
            return [FireBall(row, col, mass, speed, 0),FireBall(row, col, mass, speed, 2),FireBall(row, col, mass, speed, 4),FireBall(row, col, mass, speed, 6)]
        else:
            return [FireBall(row, col, mass, speed, 1),FireBall(row, col, mass, speed, 3),FireBall(row, col, mass, speed, 5),FireBall(row, col, mass, speed, 7)]
    else: return []

def afterMove(matrix):
    """
    matrix에서 2개 이상 있는 파이어볼 이동 후 연산 수행
    """
    fireballList = [] # 항상 초기화 하면 안되지 않나
    for i, row in enumerate(matrix):
        for j, fList in enumerate(row):
            fireBallCnt = len(fList)
            if fireBallCnt >= 2:
                # 파이어볼 합치고,
                # 4개로 나눠서 질량 sum/5, 속력 sum/갯수, 방향은 sum 홀짝 여부에 따라 분배
                sumMass = 0
                sumSpeed = 0
                directionSet = set()
                for fb in fList:
                    sumMass += fb.mass
                    sumSpeed += fb.speed
                    directionSet.add(fb.direction % 2)
                fbList = makeFourFireball(i, j, sumMass, sumSpeed, directionSet, fireBallCnt)
                matrix[i][j] = fbList
                fireballList.extend(fbList)
                # print(f'{i},{j}에서 fbList에 {printFbList(fbList)}추가됨')
            elif fireBallCnt == 1:
                fireballList.extend(fList)
    return fireballList

def printFbList(fbList):
    if len(fbList) > 0:
        print('[',end='')
        print(*fbList,end='')
        print(']',end=' ')
        
    else:
        print('[X]', end=' ')

def getSum(fireballList):
    massSum = 0
    for fb in fireballList:
        massSum += fb.mass
    return massSum

if __name__ == "__main__":
    n, m, k = map(int, input().split()) # size, num of fireball, count
    fireballList = []
    needToWatch = []
    for _ in range(m):
        ri, ci, mi, si, di = map(int, input().split())
        fireball = FireBall(ri-1, ci-1, mi, si, di)
        fireballList.append(fireball)
    
    for i in range(k):
        # 이동
        matrix = [[[]for _ in range(n)]for _ in range(n)]
        moveFireball(matrix, fireballList)
        fireballList = afterMove(matrix)
        
    print(getSum(fireballList))
