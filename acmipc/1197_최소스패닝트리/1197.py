from sys import stdin
input = stdin.readline

# kruskal algorithm : weight 최소부터 greedy하게(cycle 만들지 않도록) n-1개의 edge 선택

def find(node):
    global node_list
    if node_list[node] == node: # root인 경우
        return node
    else:
        # recursion case
        node_list[node] = find(node_list[node])
        return node_list[node]

def union(node1, node2):
    global node_list
    node1_root = find(node1)
    node2_root = find(node2)
    node_list[node1_root] = node2_root

if __name__ == "__main__":
    v, e = map(int, input().split())
    # make v nodes
    node_list = [i for i in range(v)] # i : 집합의 대표노드 (for union-find) -> 가장 작은 번호를 대표값으로
    edge_info_list = []
    for _ in range(e):
        a, b, c = map(int, input().split())  # a,b노드가 c weight로 연결됨
        edge_info_list.append((a, b, c)) # node1, node2, weight
    sorted_edge_info_list = sorted(edge_info_list, key=lambda x: x[2])
    # 작은 것부터, cycle 만들지 않도록...
    total_sum = 0
    tree_size = 0
    for edge in sorted_edge_info_list:
        node1, node2, weight = edge
        node1 -= 1
        node2 -= 1
        if find(node1) != find(node2):
            union(node1, node2)
            total_sum += weight
            tree_size += 1
        else:
            # 같은 집합에 있다면 사이클이 생성될 것임
            pass
        if tree_size == v-1:
            # mst 완성
            break
    print(total_sum)