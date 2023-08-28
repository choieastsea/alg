class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        remove duplicate in non-decreasing list
        """
        k = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                # 중복 발생
                pass
            else:
                # 다르다면, nums 배열에 넣어줌
                nums[k] = nums[i]
                k += 1
        return k