from sys import stdin
from collections import defaultdict

input = stdin.readline


def findTrees(graph: defaultdict(list), n) -> int:
    """
    graph의 엣지가 주어졌을 때, tree의 갯수를 리턴한다 
    """
    cnt = 0
    visited = [False for _ in range(n)]

    def dfs(node: int):
        # node에서부터 dfs 하여 완료된다면 1 리턴
        # 또 마주치는 경우 있다면(트리 아니므로) 0 리턴한다!
        stack = [(node, -1)] # node 번호, 직전 parent
        visited[node] = True
        while stack:
            cur, parent = stack.pop()
            for adj_node in graph[cur]:
                if not visited[adj_node]:  # not visited
                    visited[adj_node] = True
                    stack.append((adj_node,cur))
                elif visited[adj_node] and adj_node != parent:  # 이미 방문한 경우
                    # cycle
                    return 0
                elif adj_node == cur:
                    # self cycle
                    return 0
        # 현재까지 트리 방문처리하고 1 리턴하면 됨(하나의 트리라고 간주 가능)
        return 1
    for i in range(n):
        if not visited[i]:
            # i에서부터 dfs
            cnt += dfs(i)
    return cnt

case_num = 1
while True:
    n, m = map(int, input().split())  # 정점 갯수(<=500), 엣지 수
    if (n, m) == (0, 0):
        break
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    trees = findTrees(graph, n)
    if trees == 0:
        comment = 'No trees.'
    elif trees == 1:
        comment = 'There is one tree.'
    else:
        comment = f'A forest of {trees} trees.'
    print(f'Case {case_num}: {comment}')
    case_num += 1
