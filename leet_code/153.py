class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        rotated array에서 min 값의 위치를 찾자! -> BS
        """
        strt = 0
        end = len(nums)-1
        current_min = (strt, nums[strt]) # (idx, value)
        while strt <= end:
            # print(f'{strt}~{end}, current_min:{current_min}')
            mid = (strt + end) // 2
            if nums[mid] < current_min[1]:
                current_min = (mid, nums[mid])
            if nums[strt] < nums[end]:
                # 순수 증가 구간
                if nums[strt] < current_min[1]:
                    return nums[strt]
                else:
                    return current_min[1]
            elif nums[strt] < nums[mid]:
                # 앞부분 증가, 뒷부분 rotate
                if nums[strt] < current_min[1]:
                    current_min = (strt, nums[strt])
                # 뒷부분도 봐야함
                strt = mid + 1
            else:
                # 뒷부분 증가, 앞부분 rotate
                if nums[end] < current_min[1]:
                    current_min = (end, nums[end])
                # 앞부분도 봐야함
                end = mid -1
        return current_min[1]