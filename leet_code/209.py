class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        window_sum = 0
        strt = 0
        result = len(nums)
        for end in range(len(nums)):
            # print(f'strt :{strt}, end : {end}')
            window_sum += nums[end]  # 일단 0~i까지 더한다
            while window_sum >= target:  # 시작지점을 앞으로 당긴다
                # print(f'{strt}~{end} : {window_sum}')
                result = min(result, end-strt+1)
                window_sum -= nums[strt]
                strt += 1
        return result