import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    row = list(map(int, input().split()))   # n-size
    for el in row:
        heappush(heap, el)
    while len(heap) > 2*n:
        heappop(heap)
print(sorted(heap, reverse=True)[n-1])