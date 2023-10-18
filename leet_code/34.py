class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        strt = 0
        end = len(nums)-1
        
        while strt <= end:
            mid = (strt + end) // 2
            if nums[mid] < target:
                # strt : target보다 작은 최대의 지점 -> 종료시 target에 위치해야함
                strt = mid + 1
            else:
                end = mid - 1

        if (strt < len(nums) and nums[strt] != target) or strt >= len(nums):
            return [-1,-1]

        a = strt
        strt = 0
        end = len(nums)-1    
        while strt <= end:
            # print(strt,'~',end, 'mid : ',(strt+end)//2)
            mid = (strt + end) // 2
            if nums[mid] <= target:
                # strt : target보다 작거나 같은 최대의 지점 -> 종료시 target 바로 뒤에 위치해야함
                strt = mid + 1
            else:
                end = mid - 1
        # print(strt,end)
        b = strt - 1
        return [a,b]