from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    v, e = map(int, input().split())
    graph = [[] for _ in range(v)]
    for _ in range(e):
        # a~b 까지 c만큼 걸림
        a,b,c = map(int, input().split())
        graph[a-1].append((b-1,c))
    # 0번도시에 출발하여 모든 도시까지의 최단 경로 탐색 : bellman-ford
    distance = [float('inf') for _ in range(v)]
    distance[0] = 0
    for edge_cnt in range(v-1):
        # edge의 갯수를 최대 edge_cnt 만큼 사용했을 때의 최단거리
        for node, adj_list in enumerate(graph):
            # 모든 그래프의 노드에서 인접 노드를 거친 것이 더 빠른지 업데이트
            for adj_node, d in adj_list:
                distance[adj_node] = min(distance[adj_node], distance[node] + d)
    # 음수 사이클 판단 => 업데이트 또 되는 경우
    for node, adj_list in enumerate(graph):
        # 모든 그래프의 노드에서 해당 인접 노드를 거친 것이 더 빠른지 업데이트
        for adj_node, d in adj_list:
            if distance[adj_node] > distance[node] + d:
                print(-1)
                exit(0)
    for i in range(1,v):
        print(distance[i] if distance[i] != float('inf') else '-1')

    