from sys import stdin
input = stdin.readline

MAX = 100_000*100+1
if __name__ == "__main__":
    # floyd-warshall algorithm
    n, m = int(input()), int(input())  # 도시의 갯수, 간선 갯수
    # row : strt, col : end, value : distance
    graph = [[MAX for _ in range(n)]for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())  # a~b까지의 거리가 c (단방향)
        graph[a-1][b-1] = min(graph[a-1][b-1], c)
    # 모든 노드를 순회하면서, 각 노드를 거쳐 가는 거리를 업데이트한다
    for k in range(n):
        # k번 노드를 거쳐서 strt ~ end 까지 가는 거리를 구한다
        for strt, row in enumerate(graph):
            for end, el in enumerate(row):
                graph[strt][end] = min(
                    graph[strt][end], graph[strt][k] + graph[k][end])
    for i, row in enumerate(graph):
        # diagonal elements must be 0!
        row[i] = 0
        print(" ".join(list(str(el) if el != MAX else '0' for el in row)))
