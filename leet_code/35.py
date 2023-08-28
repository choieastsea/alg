class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        strt = 0
        end = len(nums)-1
        while strt <= end:
            mid = (strt + end) //2
            if nums[mid] >= target:
                end = mid - 1
            else:
                strt = mid + 1
        return strt