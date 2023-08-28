from typing import List


class Solution:
    def sort(self, nums):
        """
        sort with merge
        1. divide into 2 list (basic case: 1 element)
        2. merge 
        """
        if len(nums) <= 1:
            return nums
        else:
            length = len(nums)
            nums1 = self.sort(nums[:length//2]) + [0]*(length-length//2) # nums1에다가 merge해야하므로 0 추가
            nums2 = self.sort(nums[length//2:])
            self.merge(nums1, length//2, nums2, length-length//2)
            return nums1

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        m : length of nums1 with ignoring zero(0)
        n : length of nums2
        merge two lists into nums1 in non-decreasing order!!
        """
        # 두배열에서 뒤에서 하나씩 보면서 더 큰걸 배치하자! (nums 배열에서 처리)
        idx1, idx2 = m-1, n-1
        for i in range(m+n-1, -1, -1):
            if idx1 >= 0 and idx2 >= 0:
                if nums1[idx1] > nums2[idx2]:
                    nums1[i] = nums1[idx1]
                    idx1 -= 1
                else:
                    nums1[i] = nums2[idx2]
                    idx2 -= 1
            else:
                break
        # print(nums1, idx1, idx2)
        if idx1 < 0:
            for i in range(0, idx2+1):
                nums1[i] = nums2[i]

sol = Solution()
nums = [6, 5, 3, 2, -1, 4]
print(sol.sort(nums))
print(sol.sort([5,5,5,5,-4,0,7]))
