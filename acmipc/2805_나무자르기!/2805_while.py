import sys

input = sys.stdin.readline

def calcSum(h):
    """
    높이가 h일때, 가져갈 수 있는 나무 길이의 합을 리턴
    """
    global heights
    tree = 0
    for height in heights:
        if height > h:
            tree += (height - h)
    return tree

def findM():
    """
    calcSum()은 감소함수
    calcSum(k) >= m 인 최대의 k를 리턴
    """
    # print(f'findM({low},{high}), mid = {(low+high)//2} => {calcSum((low+high)//2)}')
    global m, cnt
    strt = 1 # 1 ~ 1,000,000
    end = max(heights)
    
    while strt <= end:
        mid = (strt + end) // 2
        sumTree = calcSum(mid)
        if sumTree >= m:
            strt = mid + 1
        else:
            end = mid - 1
    return strt - 1

if __name__ == "__main__":
    n, m = map(int, input().split()) # n ~ 100만, m ~ 20억
    heights = tuple(map(int, input().split())) # 각 높이 ~ 10억
    print(findM())
