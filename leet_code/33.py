class Solution:
    def search(self, nums: List[int], target: int) -> int:
        strt = 0
        end = len(nums)-1
        while strt <= end:
            # print(f'while : nums[{strt}]({nums[strt]})~nums[{end}]({nums[end]})')
            mid = (strt + end) //2
            if nums[mid] == target:
                return mid

            if nums[end] > nums[strt]:
                # 여기는 순수 증가하는 구간임 -> BS
                return self.bs(nums, strt, end, target) 
            elif nums[mid] > nums[strt]:
                # 뒷구간에서 rotate 발생 (앞부분 sort -> 앞부분 bs)
                result = self.bs(nums, strt, mid-1, target)
                if result == -1:
                    # rotate된 뒷구간에서 다시 시작
                    strt = mid + 1
                else:
                    return result
            else:
                # 앞구간에서 rotate 발생 (뒷부분 sort)
                result = self.bs(nums, mid+1, end, target)
                if result == -1:
                    # rotate된 앞구간에서 다시 시작
                    end = mid -1
                else:
                    return result
        return -1

    def bs(self, nums, left, right, target):
        # 정렬된 구간에서 target을 찾는 함수. 없다면 -1 리턴
        while left <= right:
            mid = (left + right)//2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1