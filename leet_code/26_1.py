class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        remove duplicate in non-decreasing list
        """
        after_mod = sorted(list(set(nums)))
        for i in range(len(after_mod)):
            nums[i] = after_mod[i]
        return len(after_mod)