from sys import stdin
from collections import deque

input = stdin.readline

NOT_VISITED = -1

if __name__ == "__main__":
    n, k = map(int, input().split()) # 현재, 목표
    # 한번에 x -> x-1, x+1, 2*x 로 이동 가능, n->k까지 최소 몇번만에 갈 수 있는지, 그리고 그 경우의 수
    q = deque()
    time_log = [NOT_VISITED for _ in range(max(n,k)+2)] # time_log[i] : i번째 장소를 몇시에 도착했는지 (-1은 도착한 적 없음)
    q.append((n,0))
    time_log[n] = 0

    min_time_to_k = 10**8
    min_time_cnt = 0

    while len(q) > 0:
        point, time = q.popleft()
        # 주변 탐색하여 q에 넣기(최단 시간인 경우만 넣어주기)
        # print(time, point)
        if point == k:
            # 목적지 도달한 경우, 최소 경로 갱신
            if min_time_to_k > time:
                min_time_to_k = time
                min_time_cnt = 1
            elif min_time_to_k == time:
                min_time_cnt += 1
            continue
        next_points = [point+1, point-1, point*2]
        for next_point in next_points:
            if next_point <= len(time_log) - 1 and next_point >= 0:
                if time_log[next_point] == NOT_VISITED:
                    q.append((next_point, time + 1))
                    time_log[next_point] = time + 1
                elif time_log[next_point] >= time + 1:
                    # 최소 시간 갱신
                    q.append((next_point, time+1))
                    time_log[next_point] = time+1
    print(min_time_to_k)
    print(min_time_cnt)