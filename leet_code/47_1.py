class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # nPk/(a!* .. *c!) 의 경우의 수
        n = len(nums)
        permset= set()
        visited = [False for _ in range(n)]
        def dp(perm):
            if len(perm) == n:
                permset.add(perm)
                return
            for i in range(n):
                if not visited[i]:
                    visited[i] = True
                    dp(perm + (nums[i],))
                    visited[i] = False
        dp(())
        return list(permset)