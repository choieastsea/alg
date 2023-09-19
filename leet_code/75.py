class Solution1:
    def sortColors(self, nums: List[int]) -> None:
        """
        배열을 순회하며 0,1,2의 갯수를 센 이후,
        배열을 다시 순회하며 값을 넣어줌
        """
        cnt0 = 0
        cnt2 = 0
        for num in nums:
            if num == 0:
                cnt0 += 1
            elif num == 1:
                pass
            else:
                cnt2 += 1
        cnt1 = len(nums)-cnt0-cnt2
        for i in range(len(nums)):
            if cnt0 > 0:
                nums[i] = 0
                cnt0 -= 1
            elif cnt1 > 0:
                nums[i] = 1
                cnt1 -= 1
            else:
                nums[i] = 2
                cnt2 -= 1


class Solution2:
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag Algorithm
        pointer 위치에 있는 값을 확인하며,,,
        2를 만나면 현재까지의 맨 뒤(right)로 스왑하여 보낸다 & --left
        1을 만나면 ++pointer
        0을 만나면 현재까지의 맨 앞과 스왑하여 보낸다 & ++strt & ++pointer
        """
        left, right, pointer = 0, len(nums)-1, 0
        while pointer <= right:
            if nums[pointer] == 2:
                # swap pointer ~ right
                nums[pointer], nums[right] = nums[right], nums[pointer]
                # move right to forward
                right -= 1
            elif nums[pointer] == 1:
                # move pointer
                pointer += 1
            else:  # 0
                # swap pointer ~ left
                nums[pointer], nums[left] = nums[left], nums[pointer]
                # move pointer
                pointer += 1
                # move left to backward
                left += 1
