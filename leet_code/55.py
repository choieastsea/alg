class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        마지막까지 갈 수 있나?
        DP[i] : 0에서 출발해서 i까지 도착할 수 있는지 여부
        """
        DP = [False for _ in range(len(nums))]
        DP[0] = True
        for i in range(len(nums)):
            if DP[i]:
                for k in range(i, min(i+nums[i]+1, len(nums)-1)):
                    DP[k] = True
        return DP[len(nums)-1]