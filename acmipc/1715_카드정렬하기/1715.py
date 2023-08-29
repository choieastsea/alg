from sys import stdin
from heapq import heapify, heappop, heappush
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    # print(arr)
    heapify(arr)
    heap = arr
    acc = 0
    while len(heap) > 1:
        """
        arr에서 가장 작은 것 두개를 더해준다... 이를 하나 남을때까지 반복한다
        """
        small1 = heappop(heap)
        small2 = heappop(heap)
        acc += (small1 + small2)
        heappush(heap, small1+small2)
    print(acc)
