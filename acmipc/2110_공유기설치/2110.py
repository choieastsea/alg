from sys import stdin
input = stdin.readline

def countRouter(period, locations):
    """
    간격이 period 이상이고, locations에 집이 위치할 때, 공유기의 갯수
    """
    global n

    point = 0
    cnt = 1 # locations[i]와 locations[point]의 차이가 period 이상이라면 cnt += 1
    for i in range(1,n):
        # print(locations[point],locations[i],  period)
        if locations[i] - locations[point] >= period:
            cnt += 1
            point = i
    # print('cnt:',cnt)
    return cnt
    

def solution(locations, c):
    """
    locations에 집들이 위치할 때,
    공유기 거리의 최소값을 리턴

    공유기 최소 거리 k로 했을 때, 공유기 설치 갯수 g(k) : g(k)는 감소함수, g(k)가 c이상일 때, k의 최댓값을 리턴한다
    """
    strt = 1
    end = max_num

    while strt <= end:
        # print(f'strt: {strt}, end:{end}, countRouter({(strt+end)//2})')
        mid = (strt + end) // 2
        counts = countRouter(mid, locations)
        # 정답구간이라면 구간 줄이기 -> 3 2 2 2 1 에서 2 이상...
        if counts >= c:
            strt = mid + 1
        else:
            end = mid - 1
    return strt - 1


if __name__ == "__main__":
    """
    n(~200,000)개의 locations(각각 ~ 1,000,000,000)에 위치한 집들이 있고, 공유기가 c개가 있을 때,
    가장 인접한 공유기 둘 사이 거리의 최댓값은?
    최대한 멀리 배치..?
    """
    n, c = map(int, input().split())
    locations = []
    max_num = 0
    for _ in range(n):
        num = int(input())
        if num > max_num:
            max_num = num
        locations.append(num)
    locations.sort() # locations가 소팅되어 있어야 countRouter가 가능함
    print(solution(locations, c))