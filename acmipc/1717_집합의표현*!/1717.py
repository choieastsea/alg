from sys import stdin
input = stdin.readline

UNION = 0
FIND = 1


class Node:
    def __init__(self, num: int) -> None:
        self.num: int = num
        self.parent: Node = None

    def __str__(self) -> str:
        return f'{self.num}'

def find(node:Node):
    """
    node가 속한 트리의 루트를 찾는다
    """
    current_node = node
    while True:
        if current_node.parent is not None:
            current_node = current_node.parent
        else:
            # current_node가 루트인 경우
            if node != current_node and node.parent != current_node:
                node.parent = current_node # path compression (입력 노드의 부모를 루트로 업데이트 해줌)
            return current_node

if __name__ == "__main__":
    n, m = map(int, input().split())
    set_node_list = [Node(i) for i in range(n+1)]  # 0,1,2,3,...
    for _ in range(m):
        op, a, b = map(int, input().split())
        a_root:Node = find(set_node_list[a])
        b_root:Node = find(set_node_list[b])
        if op == UNION:
            """
            a가 속한 집합과 b가 속한 집합을 합친다
            -> b의 루트를 find해서 a의 루트를 부모로 하도록 한다 (or a를 부모로 해도 되지만 깊이가 늘어나니까)
            """
            if a_root == b_root:
                pass
            else:
                b_root.parent = a_root
        elif op == FIND:
            """
            a와 b가 같은 집합에 속하는지 확인하여 출력한다
            -> a의 루트와 b의 루트가 같은지 확인하여 출력한다
            """
            print('YES' if b_root == a_root else 'NO')
            pass
        else:
            raise ValueError
