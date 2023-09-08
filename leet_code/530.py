# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        """
        가장 적은 두 노드간의 차이를 리턴
        : 어떠한 서브트리에서, min(본인 - 본인 왼쪽 서브 트리중 가장 큰 값, 본인 - 본인 오른쪽 서브 트리중 가장 작은 값)
        오른쪽(혹은 왼쪽) 자식에서의 최솟값과 본인 노드에서 얻을 수 있는 최솟값을 비교하여 본인의 최솟값으로 정함
        """
        node = root
        leftMin = rightMin = 10**5
        if node.right is not None:
            # 오른쪽 자식 있다면
            rightMin = min(self.getMinimumDifference(node.right), self.getSmallest(node.right) - node.val)
        if node.left is not None:
            # 왼쪽 자식 있다면
            leftMin = min(self.getMinimumDifference(node.left), node.val - self.getLargest(node.left))
        return min(rightMin, leftMin)


    def getLargest(self, node:Optional[TreeNode])-> int:
        """
        해당 노드를 루트로 하는 서브트리에서 가장 큰 값을 리턴
        """
        while node.right is not None:
            node = node.right
        return node.val

    def getSmallest(self, node:Optional[TreeNode])->int:
        """
        해당 노드를 루트로 하는 서브트리에서 가장 작은 값을 리턴
        """
        while node.left is not None:
            node = node.left
        return node.val