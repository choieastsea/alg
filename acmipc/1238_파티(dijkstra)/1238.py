from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
input = stdin.readline

INF = float('inf')

def dijkstra(strt, end=None):
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
    if end is None:
        return dist_list
    else:
        return INF

n,m,x = map(int, input().split()) # 마을 n개, m개 간선, x번 마을에서 모임
adj_list = defaultdict(list)
for _ in range(m):
    a,b,c = map(int, input().split())
    adj_list[a].append((c,b)) # 거리, 도시

# x에서 모든 도시로 가는 경로
dist_list = dijkstra(strt=x)
max_dist = 0
for i in range(1,n+1):
    if i != x:
        # i ~ x + x ~ i
        max_dist = max(max_dist, dijkstra(i,x) + dist_list[i])
print(max_dist)
