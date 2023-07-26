import sys
from collections import deque
input = sys.stdin.readline

# queue에다가 넣을 때, (index, depth)를 넣어줘볼까?
if __name__ == "__main__":
    start, finish = map(int, input().split())
    if start > finish:
        print(start-finish)
        exit(0)
    elif start == finish :
        print(0)
        exit(0)
    visited = [False for _ in range(finish+2)] # visited[i] : i번째 장소를 방문 했는지 여부
    q = deque()
    q.append((start,0))

    while True:
        # print(q)
        current_point, distance = q.popleft()
        visited[current_point] = True # 현재 노드 방문처리
        for next_point in [current_point-1, current_point+1, current_point*2]:
            if next_point == finish:
                print(distance + 1)
                exit(0)
            if next_point >= 0 and next_point <= finish+1 and not visited[next_point]: # 범위 안에 있고 방문하지 않은 경우에만 q에 추가
                q.append((next_point, distance + 1))
            
        
