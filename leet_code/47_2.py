class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # using Counter
        numsCounter = Counter(nums)
        permList = []
        n = len(nums)
        def bt(perm):
            if len(perm) == n:
                # basic case
                permList.append(perm)
                return
            for key in numsCounter: # 1,1,2 => {1:2, 2:1} 이므로,
                if numsCounter[key] > 0:
                    numsCounter[key] -= 1
                    bt(perm + [key])
                    numsCounter[key] += 1
        bt([])
        return permList