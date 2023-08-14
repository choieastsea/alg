from sys import stdin
from collections import deque

input = stdin.readline

if __name__ == "__main__":
    # F층 건물, S층에서 G층까지 엘레베이터. U층 올라가기 또는 D층 내려가기만 가능(가능한 경우만 움직임) => 몇번 버튼 눌러야하나?
    F, S, G, U, D = map(int, input().split()) # 1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000
    # 이걸 보고 BFS를 떠올리라고?~?
    if G == S:
        print(0)
    else:
        visited = [False for _ in range(F+1)]
        q = deque()
        q.append((S,0)) # (지점, 버튼 횟수)
        visited[S] = True
        while len(q) > 0:
            current = q.popleft()
            floor, cnt = current
            if floor + U <= F and not visited[floor+U]:
                q.append((floor+U,cnt+1))
                visited[floor+U] = True
                if floor+U == G:
                    print(cnt+1)
                    exit(0)
            if floor - D > 0 and not visited[floor-D]:
                q.append((floor-D,cnt+1))
                visited[floor-D] = True
                if floor-D == G:
                    print(cnt+1)
                    exit(0)
        print('use the stairs')