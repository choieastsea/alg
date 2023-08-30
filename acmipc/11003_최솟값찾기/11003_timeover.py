from collections import deque
from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    # 1 ≤ L ≤ N ≤ 5,000,000 (n:배열의 크기, l:구간의 크기)
    n, l = map(int, input().split())
    arr = list(map(int, input().split()))
    # 구간에서 제일 작은 값 중 가장 왼쪽의 있는 값의 인덱스
    min1Ind = 0 if (l == 1 or arr[0] <= arr[1]) else 1
    # print(min1Ind)
    result = [arr[0]]
    window = deque([0])
    for i in range(1,l):
        window.append(arr[i])
        if arr[min1Ind] > arr[i]:
            min1Ind = i
        result.append(arr[min1Ind])
    # print(window, min1Ind)
    for i in range(l, len(arr)):
        # [i-l+1, i]구간 중 최솟값을 출력한다
        willCome = arr[i]
        willPop = window[0]
        currentMin = window[min1Ind]
        # print(f'기존 : {window}에 {willCome}들어오고, {willPop}나갈 예정, 현재 minInd : {min1Ind}({currentMin})')
        if willCome < currentMin:
            # 가장 작은 값 업데이트되야 하는 경우
            min1Ind = l-1
        else:
            if min1Ind == 0:
                # 가장 작은값 window에서 pop 되야함
                if l != 1:
                    nextMinInd = 1  # 1번째부터 보면 됨
                    for k in range(1, l):
                        if window[nextMinInd] > window[k]:
                            nextMinInd = k
                    # 새로 들어올 것과 비교
                    if window[nextMinInd] > willCome:
                        nextMinInd = l
                    min1Ind = nextMinInd - 1
                else:
                    min1Ind = 0  # 크기 1일 때는 항상 minInd=0 되야함
            else:
                # 그대로 유지 (업데이트 되는 것 없음)
                min1Ind -= 1
        window.popleft()
        window.append(arr[i])
        # print(f'after : {window}/ 현재 minInd : {min1Ind}({window[min1Ind]})')
        result.append(window[min1Ind])
    print(*result)
