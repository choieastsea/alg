from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        BFS 탐색하면서 오른쪽 노드만 넣는다
        만약 오른쪽 없고 왼쪽만 있는 경우도 고려해야할듯
        """
        q = deque()
        if root is not None:
            q.append((root,0)) # (node, depth)
        result = []
        while len(q) > 0:
            current, depth = q.popleft()
            # print(current.val, depth)
            if len(result)-1 >= depth:
                result[depth] = current.val # 제일 오른쪽이 마지막에 덮어씌워질것임
            else:
                result.append(current.val)
            if current.left is not None:
                q.append((current.left, depth + 1))
            if current.right is not None:
                q.append((current.right, depth + 1))
        
        return result