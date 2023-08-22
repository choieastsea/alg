from sys import stdin
input = stdin.readline

# kruskal algorithm : weight 최소부터 greedy하게(cycle 만들지 않도록) n-1개의 edge 선택
if __name__ == "__main__":
    v, e = map(int, input().split())
    # make v nodes
    # node_list[i] : i node에 대하여 [(연결노드, weight), ... ]
    node_list = [[] for _ in range(v)]
    edge_info_list = []
    for _ in range(e):
        a, b, c = map(int, input().split())  # a,b노드가 c weight로 연결됨
        edge_info_list.append((a, b, c))
        node_list[a-1].append((b-1, c))
        node_list[b-1].append((a-1, c))
    sorted_edge_info_list = sorted(edge_info_list, key=lambda x: x[2])
    mst_node_set = set() # 둘다 있다면 cycle 있다고 판단
    edge_sum = 0
    # 작은 것부터, cycle 만들지 않도록...
    for edge in sorted_edge_info_list:
        strt_node = edge[0]-1
        end_node = edge[1]-1
        weight = edge[2]
        prev_len = len(mst_node_set)
        mst_node_set.add(strt_node)
        mst_node_set.add(end_node)
        after_len = len(mst_node_set) # 크기 바뀌었다면 cycle 생성 안됨
        """
        문제점 : set의 크기가 변하지 않았다고 사이클이 생성되는 것이 아니다!!
        반례) greedy하게 만드는 과정에서 두 덩어리가 연결되는 경우, 이미 둘다 set에 있지만 cycle이 생성되는 것은 아님!
        """
        if prev_len != after_len:
            edge_sum += weight
        if after_len == v:
            break
    print(edge_sum)
