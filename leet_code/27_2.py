class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        val마주치면 pass and cnt +=1
        """
        k = 0 
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i] 
                k += 1
        return k