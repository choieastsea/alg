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

def findM(low, high):
    """
    heights의 나무들을 특정 높이 h로 잘랐을 때, 잘리는 나무 길이의 합이 m을 넘도록 하는 최대의 h
    - 0부터 자르기엔 100만*20억의 연산 수행해야함 (BF는 X)
    + f(h) >= m 인 최소의 m 찾기 && f는 커팅 높이가 높을수록 감소하는 감소함수(즉 정렬됨) -> 이분 탐색
    """
    # print(f'findM({low},{high}), mid = {(low+high)//2} => {calcSum((low+high)//2)}')
    global m, cnt
    
    if low > high:
        # basic case
        return high
    
    # mid = (low + high + 1) //2
    mid = (low + high) // 2 # 중간 정수 (소수점 버림)

    sum_tree = calcSum(mid)
    # print(sum_tree)
    if sum_tree < m:
        # 부족하면 높이를 낮춰야함
        high = mid - 1
        return findM(low, high)
    elif sum_tree > m:
        # 남는다면 높이를 높여야함
        low = mid + 1
        return findM(low, high)
    else:
        return mid

if __name__ == "__main__":
    n, m = map(int, input().split()) # n ~ 100만, m ~ 20억
    heights = tuple(map(int, input().split())) # 각 높이 ~ 10억
    high = max(heights)
    low = 1
    print(findM(low, high))

# https://develop247.tistory.com/361 -> 왜 1부터 시작해야하는가?