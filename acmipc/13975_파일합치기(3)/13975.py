from sys import stdin
from heapq import heapify, heappop, heappush
input = stdin.readline

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n, files = int(input()), list(map(int, input().split()))
        heapify(files)
        total = 0
        while len(files) >= 2:
            min1 = heappop(files)
            min2 = heappop(files)
            heappush(files, min1 + min2)
            total += min1 + min2
        # print(files)
        print(total)