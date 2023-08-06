from sys import stdin
input = stdin.readline

def getTreeRadius(node_list):
    """
    node_list에서 가장 거리가 먼 두 노드의 거리를 리턴
    dfs로 하면 되지 않을까
    """
    max_distance = -1
    for i in range(len(node_list)):
        # 모든 노드를 돌아다니면서 가장 먼 거리를 측정 ... 시간이 오래 걸릴 것!
        visited = [False for _ in range(n)]
        visited[i] = True
        stack = [(i,0)] # (노드번호, 거리)
        while len(stack) > 0:
            node1, distance1 = stack.pop()
            if distance1 > max_distance:
                max_distance = distance1
            neighborNodes = node_list[node1]
            for node2, distance2 in neighborNodes:
                if not visited[node2]:
                    stack.append((node2, distance1 + distance2))
                    visited[node2] = visited
    return max_distance

if __name__ == "__main__":
    n = int(input())
    node_list = [[] for _ in range(n)] # i번 노드에서 (연결된 노드, 가중치)의 리스트
    for _ in range(n-1): # node : n, edge : n-1 (트리니까)
        a, b, weight = map(int, input().split())
        node_list[a-1].append((b-1,weight))
        node_list[b-1].append((a-1,weight))
    print(getTreeRadius(node_list))
