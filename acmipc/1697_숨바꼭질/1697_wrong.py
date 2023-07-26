import sys
from collections import deque
input = sys.stdin.readline

if __name__ == "__main__":
    start, finish = map(int, input().split())
    visited = [False for _ in range(finish+2)] # visited[i] : i번째 장소를 방문 했는지 여부
    points = [1000000 for _ in range(finish+2)] # points[i] : i번째 장소에 가는데 걸린 횟수
    q = deque()
    q.append(start)
    depth = 0
    while visited[finish] == False:
        # print(f'depth : {depth}, q: {q}')
        current_depth_points = [] # 같은 레벨에 있는 녀석들
        while len(q) > 0:   # 같은 레벨에 있는 애들을 방문처리하고 거리를 계산
            now = q.popleft()
            # print(f'{now} visit')
            visited[now] = True
            points[now] = depth
            current_depth_points.append(now)

        for now in current_depth_points:
            for next in [now-1, now+1, now*2]:
                if next >= start - 1 and next <= finish+1 and not visited[next]: # 범위 안에 있고 방문하지 않은 경우에만 q에 추가
                    q.append(next)
        depth += 1
    print(points[finish])
        
