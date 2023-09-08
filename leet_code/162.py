class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        """
        Find Peak index -> O(log(n))이라는데...
        """
        # 감소하고 있다면 왼쪽에, 증가하고 있다면 오른쪽에 극값 무조건 있을 것임
        strt = 0
        end = len(nums)-1
        if len(nums) == 1:
            return 0
        if nums[strt] > nums[strt + 1]:
            return strt
        if nums[end] > nums[end - 1]:
            return end
        strt += 1
        end -= 1
        while strt <= end:
            # print(strt,end)
            mid = (strt + end) // 2
            if nums[mid] < nums[mid+1]: # 증가 -> 오른쪽에 있음 
                strt = mid + 1
            else: # 감소 -> 왼쪽에 있음
                end = mid - 1  
                # check if mid is peak
                if nums[mid] > nums[mid-1]:
                    return mid