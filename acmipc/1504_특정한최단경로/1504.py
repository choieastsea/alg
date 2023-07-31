from sys import stdin
from heapq import heappop, heappush
input = stdin.readline

INF = 2000000000

def dijkstra(start, target):
    """
    start에서부터 최단경로를 기록, target을 마주치면 확정
    """
    global V
    visited = [False for _ in range(V)]
    path = [INF for _ in range(V)]
    path[start] = 0 # 출발지는 0!! (이거 까먹어서 틀린듯)
    pq = []
    heappush(pq, (0, start)) # (거리, 노드번호)
    while len(pq) > 0:
        # 꺼내기
        distance1, node1 = heappop(pq)
        if visited[node1]:
            continue
        visited[node1] = True
        neighbors = neighborList[node1]
        # 주변 탐색 후 거리 업데이트
        for node2, distance2 in neighbors:
            if path[node2] > distance1 + distance2 and not visited[node2]:
                path[node2] = distance1 + distance2
                # pq insert
                heappush(pq, (path[node2], node2))
    return path[target]

if __name__ == "__main__":
    V, E = map(int, input().split())
    neighborList = [[] for _ in range(V)]
    for _ in range(E):
        node1, node2, weight = map(int, input().split())
        neighborList[node1-1].append((node2-1, weight))
        neighborList[node2-1].append((node1-1, weight))
    v1, v2 = map(int,input().split()) # 꼭 거쳐야함
    # 1 ~ v1 ~ v2 ~ V 와 1 ~ v2 ~ v1 ~ V 의 거리를 비교하면 될 듯
    d1 = dijkstra(0,v1-1)
    d2 = dijkstra(v1-1,v2-1)
    d3 = dijkstra(v2-1, V-1)
    d4 = dijkstra(0,v2-1)
    d5 = dijkstra(v1-1, V-1)

    # print(d1,d2,d3)
    # print(d4,d2,d5)

    if d1 == INF or d2 == INF or d3 == INF or d4 == INF or d5 == INF:
        print(-1)
    else:
        print(min(d1+d2+d3, d4+d2+d5))