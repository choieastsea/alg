"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # 그래프를 깊은 복사하여 리턴
        # node에서부터 neighbors DFS 탐색하며 만들자
        if not node:
            return None
        root = Node(node.val)
        stack = [node] # 원본
        copyDict = {node.val : root} # 사본
        while stack:
            cur_org = stack.pop()
            # print(cur_org.val, 'popped', cur_org == copyDict[cur_org.val])
            for neighbor in cur_org.neighbors:
                # print(neighbor.val)
                # stack에 순회할 노드 추가
                if neighbor.val not in copyDict:
                    stack.append(neighbor)
                    # 없다면 새로운 노드 만들어줌
                    copyDict[neighbor.val] = Node(neighbor.val)
                # 현재 노드와 neighbor 연결
                copyDict[cur_org.val].neighbors.append(copyDict[neighbor.val])
                
        return root