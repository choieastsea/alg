class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combList = []
        def bt(comb, currentSum, curMax):
            if currentSum == target:
                # basic case
                combList.append(comb)
                return
            elif currentSum > target:
                return
            # recursion case : number can be used multiple times
            for num in candidates:
                # 작은순서대로 comb 배열에 들어가도록 함 (추가시, 현재 최대 이상의 값이 들어가도록)
                if num >= curMax:
                    bt(comb+[num], currentSum + num, num)
        bt([],0,0)
        return combList