# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # 모든 노드의 좌우를 바꾼다
        def invert(node: Optional[TreeNode]):
            if node:
                node.left, node.right = node.right, node.left
                invert(node.left)
                invert(node.right)
        invert(root)
        return root
                