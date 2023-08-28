class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        2번 이상 나타나지 않도록 중복 제거
        nums 배열 안에서 처리하기
        """
        k = 2
        for i in range(2,len(nums)):
            if nums[i] == nums[k-2]: # 3연속 같은 숫자인 경우
                pass
            else:
                nums[k] = nums[i]
                k += 1
        return k
        # nums[k]가 바뀌어서 nums[i]와 nums[i-2]가 같아져버리는 상황이 생길 수 있음
