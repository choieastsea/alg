from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop

input = stdin.readline
INF = float('inf')

def prevToPath(end, prev):
    path = [end]
    current = end
    while prev[current] != -1:
        path.append(prev[current])
        current = prev[current]
    path.reverse()
    return path

def dijkstra(strt, end):
    """
    strt에서 end까지 갈 때의 최단 거리 및 경로 리턴
    """
    dist_list = [INF for _ in range(n+1)]
    dist_list[strt] = 0
    prev = [-1 for _ in range(n+1)]
    pq = [(0,strt)] # 거리, 노드
    while pq:
        # 현재 가장 가까운 노드와 그 거리
        dist, current = heappop(pq)
        if current == end:
            # 도착지점까지 옴
            break
        adj_tuple = adj_dist_list[current]
        # 이전노드와 current까지의 거리가 이미 알고 있는 current까지의 거리보다 길면 더 볼 필요 없음
        if dist > dist_list[current]:
            continue
        for next_node, next_dist in adj_tuple:
            # 현재 노드를 거쳐 다음노드로 가는게 더 가깝다면 업데이트
            if dist + next_dist < dist_list[next_node]:
                dist_list[next_node] = dist + next_dist
                prev[next_node] = current
                heappush(pq, (dist_list[next_node], next_node))
    return dist_list[end], prev

if __name__ == "__main__":
    n = int(input()) # 도시
    m = int(input()) # 경로
    adj_dist_list = defaultdict(list) # i번 도시 = [(인접 도시 index, 거리)...]
    for _ in range(m):
        a,b,c = map(int, input().split())
        adj_dist_list[a].append((b,c))
    strt, end = map(int, input().split())
    dist, prev = dijkstra(strt,end)
    path = prevToPath(end, prev)
    print(f'{dist}\n{len(path)}\n{" ".join(list(map(str,path)))}')
