from sys import stdin
from collections import deque
input = stdin.readline

def printParent(parent_list):
    for i, parent in enumerate(parent_list):
        if i > 0:
            print(parent + 1)
def bfs(node):
    global node_list
    queue = deque()
    queue.append(node)
    parent_list = [0 for _ in range(len(node_list))] # parent_list[i] : i번 노드의 부모
    visited = [False for _ in range(len(node_list))] # visited[i] : i번 노드를 방문했는지
    while len(queue) > 0:
        current_node = queue.popleft()
        adj_list = node_list[current_node]
        for adj_node in adj_list:
            if not visited[adj_node]:
                queue.append(adj_node)
                visited[adj_node] = True
                parent_list[adj_node] = current_node # (루트에서부터 시작하여) 현재노드에서 주변 노드로 간다면, 주변 노드의 부모는 현재노드일 것
    return parent_list

if __name__ == "__main__":
    """
    트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 출력(2번 노드부터)
    """
    n = int(input())
    node_list = [[]for _ in range(n)] # node_list[i] : i번(0~n-1) 노드와 연결된 노드의 번호 리스트
    for _ in range(n-1):
        a,b = map(int, input().split())
        node_list[a-1].append(b-1)
        node_list[b-1].append(a-1)
    parent_list = bfs(0)
    printParent(parent_list)

