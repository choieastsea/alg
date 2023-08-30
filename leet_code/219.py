class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        중복된 값의 인덱스 차이가 k이상인 것이 있다면 return true
        """
        hash = {}
        for i, num in enumerate(nums):
            if hash.get(num) is not None:
                # 중복 있으니, k차이 이하인지 확인
                if abs(hash[num] - i) <= k:
                    return True
            hash[num] = i
        return False