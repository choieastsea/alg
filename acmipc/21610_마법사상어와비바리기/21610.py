from sys import stdin
input = stdin.readline

def printState():
    global bucketMatrix
    global cloudList

    for i in range(len(bucketMatrix)):
        for j in range(len(bucketMatrix[0])):
            if [i,j] in cloudList:
                print(f'[ {bucketMatrix[i][j]} ]',end='')
            else:
                print(f'  {bucketMatrix[i][j]}  ',end='')
        print()
    print()

def getDirectionInfo(direction, d):
    """
    한 칸이 얼마나 움직어야하는지 (행 이동, 열 이동)를 리턴
    """
    if direction == 1: # 좌
        return (0, -d)
    elif direction == 2: # 좌상
        return (-d, -d)
    elif direction == 3: # 상
        return (-d, 0)
    elif direction == 4: # 우상
        return (-d, d)
    elif direction == 5: # 우
        return (0, d)
    elif direction == 6: # 우하
        return (d, d)
    elif direction == 7: # 하
        return (d, 0)
    elif direction == 8: # 좌하
        return (d, -d)
    else:
        print('unexpected direction')
        exit(-1)
    


def moveCloud(direction, distance):
    """
    cloudList의 요소들을 direction 방향으로 distance씩 움직인다
    """
    global cloudList
    global n
    drow, dcol = getDirectionInfo(direction, distance)
    # print(drow, dcol, '씩 이동')
    for i, cloud in enumerate(cloudList):
        row, col = cloud
        next_row, next_col = row + drow, col + dcol
        if next_row >= n:
            next_row %= n
        elif next_row < 0:
            while next_row < 0:
                next_row += n
        if next_col >= n:
            next_col %= n
        elif next_col < 0:
            while next_col < 0:
                next_col += n
        cloudList[i] = [next_row, next_col]

def checkNearBucket(row, col):
    """
    row, col 대각선 주변 bucket에 물이 있는지 확인하여
    있는 방향의 수를 리턴한다 (0~4) -> 주변에 구름이 있다면 무조건 1 증가시켜도 됨(구름이 기존 0인 경우에도 카운트 해줘야함)
    """
    global bucketMatrix
    # row,col = 2,0 // n = 5
    cnt = 0
    if row + 1 < n and col + 1 < n:
        if cloudMatrix[row+1][col+1] or bucketMatrix[row+1][col+1] > 0:
            cnt += 1
    if row -1 >= 0 and col + 1 < n:
        if cloudMatrix[row-1][col+1] or bucketMatrix[row-1][col+1] > 0:
            cnt += 1
    if row + 1 < n and col - 1 >= 0:
        if cloudMatrix[row+1][col-1] or bucketMatrix[row+1][col-1] > 0:
            cnt += 1
    if row -1 >= 0 and col - 1 >= 0:
        if cloudMatrix[row-1][col-1] or bucketMatrix[row-1][col-1] > 0:
            cnt += 1

    return cnt

def rainInCloudAreaBug():
    """
    cloudList의 영역의 바구니에 물 1씩 증가
    구름 주변 물 있다면 1씩 추가로 증가
    """
    global cloudList
    global bucketMatrix
    for cloud in cloudList:
        row, col = cloud
        # 구름 영역에 물 1 증가
        bucketMatrix[row][col] += 1
        # 구름 주변에 있다면 구름이였던 곳 1씩 증가
        bucketMatrix[row][col] += checkNearBucket(row, col)

def createCloudMatrix(cloudList):
    """
    cloudList로 cloudMatrix 만들기
    """
    # print(f'create cloud matrix, size: {len(cloudList)}')
    newCloudMatrix = [[False for _ in range(n)]for _ in range(n)]
    for cloud in cloudList:
        i,j = cloud
        # print(i,j)
        newCloudMatrix[i][j] = True
    return newCloudMatrix

def makeCloud(cloudMatrix):
    """
    기존에 구름 없었던 부분에서 구름 만들고, 기존 구름 제거
    """
    # print('기존 구름')
    # print(cloudMatrix)
    # print('...')
    new_cloud_list = []
    for i in range(len(bucketMatrix)):
        for j in range(len(bucketMatrix[i])):
            if bucketMatrix[i][j] >= 2:
                # 물 줄이고 구름 생성
                if not cloudMatrix[i][j]:
                    bucketMatrix[i][j] -= 2
                    new_cloud_list.append([i,j])
                else:
                    # print(f'{i},{j} is cloud')
                    pass
    return new_cloud_list

def calculateSum():
    global bucketMatrix
    cnt = 0
    for row in bucketMatrix:
        cnt += sum(row)
    return cnt
            
if __name__ == "__main__":
    n,m = map(int, input().split()) # n*n size matrix & move m times
    bucketMatrix = [list(map(int, input().split())) for _ in range(n)]
    # 비바라기 마법~!
    cloudList = [[n-1,0], [n-1,1], [n-2,0], [n-2,1]]
    cloudMatrix = createCloudMatrix(cloudList)
    # print(cloudMatrix)
    # printState()
    for _ in range(m):
        direction, distance = map(int, input().split())
        # 1. di, si 만큼 비구름 이동
        moveCloud(direction, distance)
        cloudMatrix = createCloudMatrix(cloudList)
        # printState()
        # 2. 구름영역의 바구니의 물 1씩 증가
        rainInCloudAreaBug()
        # printState()
        # 3. 구름 만들기
        cloudList = makeCloud(cloudMatrix)
        cloudMatrix = createCloudMatrix(cloudList)
        # print(cloudList)
        # print(cloudMatrix)
        # printState()
    print(calculateSum())
        
