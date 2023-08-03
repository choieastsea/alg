from sys import stdin
from collections import deque

input = stdin.readline

def bfs(n):
    global game
    visited = [False for _ in range(101)]
    # 첫번째칸 방문 처리 후 queue에 넣는다
    visited[1] = 1
    q = deque() 
    q.append((1,0)) # (칸, distance)
    min_distance = 100
    while len(q) > 0:
        # print(q)
        i, distance = q.popleft()
        if i == n:
            if distance < min_distance:
                min_distance = distance
        for k in range(1,7):
            if i+k <= 100:
                to = game[i+k] # 실제 가게 되는 곳
                if visited[to] == False:
                    visited[to] = True
                    q.append((to, distance+1))
                if to == n:
                    q.append((to, distance+1))
    return min_distance

if __name__ == "__main__":
    n, m = map(int, input().split())
    game = [i for i in range(101)] # game[i] : i번칸에 도착하면, 실제 어디로 가게 되는지
    for _ in range(n):
        # 사다리 정보
        strt, end = map(int, input().split())
        game[strt] = end
    for __ in range(int(m)):
        # 뱀 정보
        strt, end = map(int, input().split())
        game[strt] = end
    # BFS로 최단경로 탐색
    print(bfs(100))