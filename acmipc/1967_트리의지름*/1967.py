from sys import stdin
input = stdin.readline

def dfs(node_list, strt_node):
    """
    node_list에서 가장 거리가 먼 두 노드의 거리를 리턴
    dfs로 하면 되지 않을까
    leaf to leaf만 확인? -> O((n^2)/2)정도라 비슷함
    (sol)
    2번의 DFS를 수행
    1. 임의의 노드에서 DFS로 가장 먼 leaf까지 탐색
    2. 해당 leaf에서 DFS로 가장 먼 다른 leaf까지 탐색
    """
    visited = [False for _ in range(n)]
    visited[strt_node] = True
    stack = [(strt_node,0)] # (노드번호, 거리)
    max_info = (0, 0)
    while len(stack) > 0:
        node1, distance1 = stack.pop()
        if max_info[1] < distance1:
            max_info = (node1, distance1)
        neighborNodes = node_list[node1]
        for node2, distance2 in neighborNodes:
            if not visited[node2]:
                stack.append((node2, distance1 + distance2))
                visited[node2] = visited
    return max_info

if __name__ == "__main__":
    n = int(input())
    node_list = [[] for _ in range(n)] # i번 노드에서 (연결된 노드, 가중치)의 리스트
    for _ in range(n-1): # node : n, edge : n-1 (트리니까)
        a, b, weight = map(int, input().split())
        node_list[a-1].append((b-1,weight))
        node_list[b-1].append((a-1,weight))
    node1, d1 = dfs(node_list, 0)
    node2, d2 = dfs(node_list, node1)
    print(d2)
