from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

input = stdin.readline
INF = float('inf')

def dijkstra(strt, end):
    """
    strt ~ end 까지의 최소 비용을 리턴 
    """
    dist_list = [INF for _ in range(n+1)]
    dist_list[strt] = 0
    pq = [(0, strt)] # 거리, 도시
    while pq:
        curDist, curCity = heappop(pq)
        if curCity == end:
            return dist_list[curCity]
        if curDist > dist_list[curCity]:
            # 연결된 노드에서의 거리가 시작에서부터 거리보다 이미 크다면 볼 필요 없음
            continue
        for nextDist, nextCity in adj_list[curCity]:
            # 주변 노드 탐색하며 dist_list update & pq에 추가
            if dist_list[curCity] + nextDist < dist_list[nextCity]:
                dist_list[nextCity] = dist_list[curCity] + nextDist
                heappush(pq, (dist_list[nextCity], nextCity))
    

if __name__ == "__main__":
    n, m = int(input()), int(input())
    adj_list = defaultdict(list)
    for _ in range(m):
        a,b,c = map(int, input().split())
        adj_list[a].append((c,b)) # 거리, 도시
    strt, end = map(int, input().split())
    print(dijkstra(strt,end))