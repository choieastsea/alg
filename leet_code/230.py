# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        왼쪽 서브트리 -> 부모 -> 오른쪽 서브트리로 순회
        """
        sortedList = []
        self.traverse(root, k, sortedList)
        return(sortedList[k-1])

    def traverse(self, node, k, sortedList):
        """
        cnt==k가 될때까지 L-N-R 순회
        """
        if node.left is not None:
            self.traverse(node.left, k, sortedList)
        # print(f'{node.val} visited!')
        sortedList.append(node.val)
        if len(sortedList) == k:
            return 
        if node.right is not None:
            self.traverse(node.right, k, sortedList)