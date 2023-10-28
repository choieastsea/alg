from sys import stdin
from collections import Counter
from heapq import heappush, heappop
input = stdin.readline

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
                    # 최대가 이미 제거된 값이라면 다음 최댓값을 지운다
                    while maxq:
                        maxVal = -heappop(maxq)
                        if maxVal in arr:
                            if arr[maxVal] == 1:
                                del arr[maxVal]
                            elif arr[maxVal] == 0:
                                # 해당 값이 이미 없는 경우, 지워주고 다음 최댓값 pop
                                del arr[maxVal]
                                continue
                            else:
                                arr[maxVal] -= 1
                            break
                    
                else:
                    # 최솟값 제거
                    while minq:
                        minVal = heappop(minq)
                        if minVal in arr:
                            if arr[minVal] == 1:
                                del arr[minVal]
                            elif arr[minVal] == 0:
                                # 해당 값이 이미 없는 경우, 지워주고 다음 최솟값 pop
                                del arr[minVal]
                                continue
                            else:
                                arr[minVal] -= 1
                            break
        if not maxq or not minq:
                # 둘 중 하나 비어있게 된 경우에는 초기화
                maxq = []
                minq = []
                arr = Counter()
        # print(arr)
    print(f'{max(arr)} {min(arr)}' if len(arr) > 0 else 'EMPTY')