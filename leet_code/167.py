class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # find two index that sum of elements is equivalent to target
        # numbers are non-decreasing order list
        n = len(numbers)
        left = 0
        right = n-1
        while True:
            result = numbers[left] + numbers[right]
            if result > target:
                right -= 1
            elif result == target:
                return [left+1, right+1]
            else:
                left += 1
            