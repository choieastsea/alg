from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, num) -> None:
        self.num = num
        self.children = []
        self.parent = None

    def hasChild(self) -> bool:
        return len(self.children) > 0
    
def cut(node: Node):
    """
    해당 노드와 부모와의 연결을 끊는다
    """
    parent = node.parent
    if parent is not None:
        parent.children.remove(node)
    
    
def countLeaf(node:Node):
    """
    해당 노드에서부터 시작하는 subtree에서 leaf node의 갯수를 리턴한다
    """
    cnt = 0
    if node.hasChild():
        for child in node.children:
            cnt += countLeaf(child)
        return cnt
    else:
        # leaf node
        return 1
    
if __name__ == "__main__":
    n = int(input())
    node_list = []
    superRootNode = Node(n)
    for i in range(n):
        node_list.append(Node(i)) # node_list[i] : Node(i)
    parent_list = list(map(int, input().split()))
    for i, parent in enumerate(parent_list):
        if parent != -1:
            node_list[parent].children.append(node_list[i])
            node_list[i].parent = node_list[parent]
        else:
            # root node는 superRootNode의 자식
            node_list[i].parent = superRootNode
            superRootNode.children = [node_list[i]]

    # 트리 자르기
    cut_node = int(input())
    cut(node_list[cut_node])

    if len(superRootNode.children) > 0:
        print(countLeaf(superRootNode))
    else:
        # root 없어진 케이스
        print(0)
