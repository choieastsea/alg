from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append((root,0)) # (node, depth)
        sum_list = []
        cnt_list = []
        while len(q) > 0:
            current, depth = q.popleft()
            # print(current.val, depth)
            if len(sum_list)-1 >= depth:
                sum_list[depth] += current.val
                cnt_list[depth] += 1
            else:
                sum_list.append(current.val)
                cnt_list.append(1)
            if current.left is not None:
                q.append((current.left, depth + 1))
            if current.right is not None:
                q.append((current.right, depth + 1))
        # print(result)
        for i in range(len(sum_list)):
            sum_list[i] = sum_list[i]/cnt_list[i]
        return sum_list