from sys import stdin
input = stdin.readline


def find(node):
    """
    node의 root를 리턴, 경로중에 root 아니면 부모를 root로 path compression
    """
    if root_list[node] != node:
        root_list[node] = find(root_list[node])
    return root_list[node]


def union(node1, node2):
    """
    두 node가 속한 집합을 합침
    -> node2의 root를 node1의 root로 
    """
    node1_root = find(node1)
    node2_root = find(node2)
    # 합침
    root_list[node2_root] = node1_root


if __name__ == "__main__":
    v, e = map(int, input().split())  # v : ~10만, e : ~100만
    root_list = [i for i in range(v)]  # root list for union-find
    # 입력을 한줄에 처리하자~ 그게 더 빠른듯
    edge_info_list = sorted([tuple(map(int, input().split())) for _ in range(e)], key=lambda x: x[2])

    weight_sum = 0
    weight_cnt = 0
    # print(root_list)
    for edge in edge_info_list:
        # 작은 weight 순서대로 union
        if weight_cnt == v-2:
            # 제일 큰 weight 제외
            break
        else:
            strt, end, weight = edge
            if find(strt-1) != find(end-1):
                # cycle 생성되지 않는다면 합침
                union(strt-1, end-1)
                weight_sum += weight
                weight_cnt += 1
    # print(root_list)
    print(weight_sum)
