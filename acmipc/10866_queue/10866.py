import sys
from collections import deque
input = sys.stdin.readline

"""
push_front X: 정수 X를 덱의 앞에 넣는다.
push_back X: 정수 X를 덱의 뒤에 넣는다.
pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 덱에 들어있는 정수의 개수를 출력한다.
empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
"""

n = int(input())
q = deque()
for _ in range(n):
    line = input()[:-1]
    if line.startswith('push_front'):
        x = line.split(' ')[1]
        q.appendleft(x)
    elif line.startswith('push_back'):
        x = line.split(' ')[1]
        q.append(x)
    elif line == 'pop_front':
        try:
            print(q.popleft())
        except:
            print(-1)
    elif line == 'pop_back':
        try:
            print(q.pop())
        except:
            print(-1)
    elif line == 'size':
        print(len(q))
    elif line == 'empty':
        print(1 if len(q) == 0 else 0)
    elif line == 'front':
        try:
            print(q[0])
        except:
            print(-1)
    elif line == 'back':
        try:
            print(q[len(q)-1])
        except:
            print(-1)
    else:
        print('err')
