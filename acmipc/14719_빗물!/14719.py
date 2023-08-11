from sys import stdin
input = stdin.readline

def sumRain(strt, end, isDirection):
    """
    strt~end까지 빗물 양 더함
    isDirection : 순방향 여부
    """
    # print(f'{strt}부터 {end}까지 더하기')
    global walls
    rain_sum = 0
    if isDirection:
        for i in range(strt+1, end):
            rain_sum += (walls[strt] - walls[i])
            walls[i] = walls[strt] # 역방향으로 돌때 비 안차게 메워버린다
    else:
        for i in range(strt-1, end, -1): # 인덱스 확인해보기
            rain_sum += (walls[strt] - walls[i])
    # print(f'rain : {rain_sum} 더하기')
    return rain_sum
    

def calculateRain(walls):
    """
    왼쪽에서부터 온 것과, 오른쪽에서부터 온 누적값의 합을 구하면 될듯?
    """
    highest = 0
    index = -1
    rain = 0
    for i in range(len(walls)):
        wall = walls[i]
        if highest <= wall:
            # 제일 높은 벽 갱신
            if highest != 0 and index != -1:
                # 여태까지 더하면 됨
                rain += sumRain(index, i, True)
            # print(f'정방향 highest 갱신 : {wall}, index 갱신 : {i}')
            highest = wall
            index = i
    # 역방향~
    highest = 0
    index = -1
    for i in range(len(walls)-1, -1, -1):
        wall = walls[i]
        if highest <= wall:
            # 제일 높은 벽 갱신
            if highest != 0 and index != -1:
                # 여태까지 더하면 됨
                rain += sumRain(index, i, False)
            # print(f'역방향 highest 갱신 : {wall}, index 갱신 : {i}')
            highest = wall
            index = i
    return rain

if __name__ =="__main__":
    H, W = map(int, input().split())
    walls = list(map(int, input().split()))
    print(calculateRain(walls))