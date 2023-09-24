from sys import stdin
from heapq import heappush, heappop
input = stdin.readline

if __name__ == "__main__":
    strt, end = map(int, input().split())
    if strt < end:
        heap = []  # 시간 순으로 작은것부터 나와야 하므로 PQ
        heappush(heap, (0, strt))
        visited = [False for _ in range(2*end+1)]
        visited[strt] = True
        while heap:
            time, cur_loc = heappop(heap)
            # print(time, cur_loc)
            # 1. 2배 증가 먼저 처리 (최소 시간)
            if cur_loc * 2 == end:
                print(time)
                exit()
            elif 2*cur_loc <= len(visited)-1 and not visited[2*cur_loc]:
                heappush(heap, (time, 2*cur_loc))
            # 2. +1, -1 처리
            if abs(cur_loc-end) == 1:
                print(time + 1)
                exit()
            else:
                if cur_loc + 1 <= len(visited) - 1 and not visited[cur_loc + 1]:
                    heappush(heap, (time + 1, cur_loc + 1))
                if cur_loc - 1 >= 0 and not visited[cur_loc - 1]:
                    heappush(heap, (time + 1, cur_loc - 1))
            # 마지막에 방문처리
            if cur_loc + 1 <= len(visited) - 1:
                visited[cur_loc + 1] = True
            if cur_loc - 1 >= 0:
                visited[cur_loc - 1] = True
            if cur_loc * 2 <= len(visited) - 1:
                visited[cur_loc * 2] = True
    elif strt > end:
        print(strt - end)
    else:
        print(0)
