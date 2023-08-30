from sys import stdin
from collections import deque
input = stdin.readline

VALUE = 0
INDEX = 1

MIN1 = 0
LAST = -1

if __name__ =="__main__":
    n,l = map(int, input().split())
    arr = list(map(int, input().split()))
    q = deque()
    for i in range(len(arr)):
        currentValue = arr[i]
        if len(q) == 0:
            q.append((currentValue,i))
        else:
            if (i-q[MIN1][INDEX]) >= l:
                # 맨 앞 pop 할 차례
                q.popleft()
            # 적당한 곳에 추가
            while len(q)>0 and q[LAST][VALUE] >= currentValue:
                q.pop()
            q.append((currentValue,i))
        print(q[MIN1][VALUE], end=' ')
    print()
        