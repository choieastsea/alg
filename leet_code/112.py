# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """
        root에서부터 leaf까지 더해서 targetSum이 되는것이 존재하는지를 반환
        """
        answer = False
        def traverse(node):
            nonlocal answer
            if not (node.left or node.right):
                # leaf -> check sum
                if node.val == targetSum:
                    answer = True
                return
            if node.left:
                node.left.val += node.val
                traverse(node.left)
            if node.right:
                node.right.val += node.val
                traverse(node.right)
        if root:
            traverse(root)
        return answer