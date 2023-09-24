from sys import stdin
from collections import deque
input = stdin.readline

if __name__ == "__main__":
    strt, end = map(int, input().split())
    if strt > end:
        print(strt-end)
    elif strt < end:
        visited = [False for _ in range(end*2+1)]
        q = deque()
        q.append((0,strt))
        while q:
            time, current = q.popleft()
            # print(time, current)
            if current == end:
                print(time)
                exit(0)
            if current*2 <= len(visited) and not visited[current*2]:
                q.appendleft((time, current*2))
                visited[current*2] = True
            if current -1 >= 0 and not visited[current-1]:
                q.append((time+1, current-1))
                visited[current-1] = True
            if current + 1 <= len(visited) and not visited[current+1]:
                q.append((time+1, current+1))
                visited[current+1] = True

    else:
        print(0)