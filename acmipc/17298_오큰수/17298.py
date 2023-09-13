from sys import stdin
from heapq import heappush, heappop

input = stdin.readline
if __name__ =="__main__":
    """
    오른쪽의 자기보다 큰 수 중 가장 왼쪽에 있는 수(NGE)를 출력
    -> 오른쪽에서부터 탐색하면서 heap의 숫자와 비교한다
    """
    n = int(input())
    arr = list(map(int, input().split()))
    arr.append(-1)
    nge = [-1 for _ in range(n+1)]
    heap = [-1]
    for i in range(n, 0, -1):
        # 뒤에서부터 이전 인덱스와 비교하며 nge[i-1]를 초기화
        # print(arr[i-1])
        if arr[i] > arr[i-1]:
            # i-1보다 i가 큼 (앞이 더 작음 -> 무조건~ nge는 바로 뒤) 
            nge[i-1] = arr[i]
            heappush(heap, arr[i])
        else:
            # 왼쪽이 더 큼 -> 과거 오른쪽 큰 애들 보면 됨
            while heap:
                el = heap[0]
                if el > arr[i-1]:
                    # 더 큰게 나올때 까지 제거
                    break
                else:
                    heappop(heap)
            if el > arr[i-1]:
                # heap의 값이 더 큼
                nge[i-1] = el
            else:
                # 여전히 제일 큼
                nge[i-1] = -1
            heappush(heap, arr[i-1])
    print(*nge[:n])