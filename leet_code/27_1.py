LARGE_NUM = 51
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        replace all val in nums to _
        and sort nums
        """
        # vals이 몇개 있는지 체크하고 51로 바꾸기
        val_cnt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                val_cnt += 1
                nums[i] = LARGE_NUM
        nums.sort()
        return len(nums)-val_cnt