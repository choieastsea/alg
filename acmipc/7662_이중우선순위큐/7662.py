from sys import stdin
from collections import Counter
from heapq import heappush, heappop
input = stdin.readline

def getMaxOrMin(isMax : bool):
    if isMax:
        while maxq:
            maxVal = -heappop(maxq)
            if maxVal in arr:
                if arr[maxVal] == 1:
                    del arr[maxVal]
                else:
                    arr[maxVal] -= 1
                break
        return maxVal
    else:
        while minq:
            minVal = heappop(minq)
            if minVal in arr:
                if arr[minVal] == 1:
                    del arr[minVal]
                else:
                    arr[minVal] -= 1
                break   
        return minVal

T = int(input())
for _ in range(T):
    maxq = []
    minq = []
    arr = Counter() # 각 숫자 몇개 남았나..
    k = int(input())
    ops = tuple(input().split() for _ in range(k))
    for op, num in ops:
        num = int(num)
        if op == 'I':
            # insert
            heappush(maxq, -num)
            heappush(minq, num)
            arr[num] += 1
        else:
            # pop (max or min)
            if len(arr) > 0:
                if num == 1:
                    # 최댓값 제거
                    getMaxOrMin(True)
                else:
                    # 최솟값 제거
                    getMaxOrMin(False)
        if not maxq or not minq:
                # 둘 중 하나 비어있게 된 경우에는 초기화
                maxq = []
                minq = []
                arr = Counter()
        # print(arr)
    if len(arr) > 1:
        print(f'{getMaxOrMin(True)} {getMaxOrMin(False)}')
    elif len(arr) == 1:
        maxVal = getMaxOrMin(True)
        print(f'{maxVal} {maxVal}')
    else:
        print('EMPTY')