from sys import stdin
input = stdin.readline

def calcNum(k):
    """
    g(k) : k cm만큼 잘랐을 때 나오는 랜선의 갯수
    """
    cnt = 0
    for length in lengths:
        cnt += length // k
    return cnt

def getMaxK(n):
    """
    g(k) >= n 인 k의 최댓값 리턴
    """
    low = 1
    high = 2**32 - 1
    while low <= high:
        mid = (low + high) // 2
        cnt = calcNum(mid)
        # print(f'{low}~{high}, g({mid}) = {cnt}')
        if cnt >= n:
            # 참인 조건 -> 쪼여
            low = mid + 1
        else:
            # 거짓인 조건 -> 줄여
            high = mid - 1
    return low - 1

if __name__ == "__main__":
    K, n = map(int, input().split())
    lengths = []
    for _ in range(K):
        length = int(input())
        lengths.append(length)
    print(getMaxK(n))