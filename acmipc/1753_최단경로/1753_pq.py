from sys import stdin
from queue import PriorityQueue

input = stdin.readline

def printPath(path):
    for el in path:
        if el == 30000000:
            print('INF')
        else:
            print(el)
        

def dijkstra(start, n):
    """
    start에서 각 간선까지 가는 최단 경로 리스트를 리턴
    """
    pq = PriorityQueue()
    visited = [False for _ in range(n)] # 거리가 확정된 인덱스는 True
    path = [30000000 for _ in range(n)]
    pq.put((0, start)) # (거리(우선순위 기준), 인덱스) 로 PQ에 넣음
    while not pq.empty():
        distance1, node1 = pq.get()
        if visited[node1]:
            # 이미 확정된 노드라면 갱신할 필요 없음
            continue
        visited[node1] = True
        # print(f'{node1} visit')
        path[node1] = distance1
        # 주변과 비교하여 pq에 넣기
        neighborOfCurrent = neighborList[node1]   
        for node2, distance2 in neighborOfCurrent:
            #   print(f'기존 {node2}까지의 거리: {path[node2]} ~ {node1}을 거쳐 {node2}로 가는 거리 : {distance1 + distance2}')
              if path[node2] > distance1 + distance2 and not visited[node2]:
                  #need to update
                  path[node2] = distance1 + distance2
                  pq.put((path[node2], node2))
        # print(f'pq : {pq.queue}, visited: {visited}, path: {path}')
    return path

if __name__ =="__main__":
    V, E = map(int, input().split())
    start = int(input())
    neighborList = [[]for _ in range(V)] # neighborList[i] : i-1번 노드와 연결된 (엣지, 거리)의 배열
    for _ in range(E):
        n1, n2, weight = map(int, input().split()) # n1에서 n2까지 연결된 간선의 weight
        neighborList[n1-1].append((n2-1, weight)) # 단방향 그래프
    path = dijkstra(start-1, V)
    printPath(path)


# 4 8
# 1
# 1 2 3
# 2 1 5
# 4 3 4
# 2 3 10
# 1 3 10
# 2 4 1
# 3 1 1
# 1 2 2
# -> 0 2 7 3
