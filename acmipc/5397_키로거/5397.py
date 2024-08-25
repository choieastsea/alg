from collections import deque


n = int(input())


for _ in range(n):
    L = input()

    left = deque()
    right = deque()

    for ch in L:
        if ch == '<':
            # 커서 왼쪽으로
            if len(left):
                right.appendleft(left.pop())
        elif ch == '>':
            # 커서 오른쪽으로
            if len(right):
                left.append(right.popleft())
        elif ch == '-':
            # backspace
            if len(left):
                left.pop()
        else:
            left.append(ch)
    print(''.join(left)+''.join(right))
