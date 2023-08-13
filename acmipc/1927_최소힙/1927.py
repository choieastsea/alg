from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    heap = []
    for _ in range(n):
        m = int(input())
        if m == 0:
            # heappop
            try:
                print(heappop(heap))
            except:
                print(0)
        else:
            heappush(heap,m)
