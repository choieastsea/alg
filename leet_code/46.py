class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        nPn 만들기! (중복 x)
        """
        permList = []
        visited = [False for _ in range(len(nums))]
        def dp(perm):
            if len(perm) == len(nums):
                permList.append(perm)
                return
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dp(perm+[nums[i]])
                    visited[i] = False
        dp([])
        return permList