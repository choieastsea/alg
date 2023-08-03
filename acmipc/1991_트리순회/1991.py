from sys import stdin
input = stdin.readline

class Node:
    def __init__(self, name) -> None:
        self.name = name
        self.lchild = None
        self.rchild = None

def preorder(node: Node):
    """
    전위 순회 : 루트 - 왼 - 오
    """
    print(node.name, end='')
    if node.lchild is not None:
        preorder(node.lchild)
    if node.rchild is not None:
        preorder(node.rchild)

def inorder(node: Node):
    """
    중위 순회 : 왼 - 루트 - 오
    """
    if node.lchild is not None:
        inorder(node.lchild)
    print(node.name, end='')
    if node.rchild is not None:
        inorder(node.rchild)

def postorder(node:Node):
    """
    후위순회 : 왼 - 오 - 루트
    """
    if node.lchild is not None:
        postorder(node.lchild)
    if node.rchild is not None:
        postorder(node.rchild)
    print(node.name, end='')
    
if __name__ == "__main__":
    n = int(input())
    node_dict = {} # "A" : Node(A)
    strt = ord("A")
    for i in range(strt, strt+n):
        node_dict[chr(i)] = Node(chr(i))
    for _ in range(n):
        node, lchild, rchild = input().split()
        if lchild != '.':
            node_dict[node].lchild = node_dict[lchild]
        if rchild != '.':
            node_dict[node].rchild = node_dict[rchild]
    preorder(node_dict["A"])
    print()
    inorder(node_dict["A"])
    print()
    postorder(node_dict["A"])
    print()
