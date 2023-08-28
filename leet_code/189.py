class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1. Brute Force -> time exceeded
        # for _ in range(k):
        #     strt = nums[-1]
        #     for i in range(len(nums)-1,0,-1):
        #         nums[i] = nums[i-1]
        #     nums[0] = strt

        # 2. only one for loop : nums[a] -> nums[(a+k)%n]로 옮겨질 것
        # n = len(nums)
        # new_list = [0 for _ in range(n)]
        # for i in range(n):
        #     new_list[(i+k)%n] = nums[i]
        # for i in range(n):
        #     nums[i] = new_list[i]
            
        # 3. do 2nd solution in single list(nums)
        n = len(nums)
        if k >= n:
            k %= n
        tmp = nums[-k:] # k개 만큼 nums에서 저장
        nums[k:] = nums[:-k] # k까지는 reverse
        nums[:k] = tmp  # k부터는 tmp 덮어씌우기
        