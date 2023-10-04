class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """
        nCk 수행 (1~n에서 k개 선택)
        bt 수행하면서, 작은것부터 확장시키는 것을 원칙으로 하면 조합 모을 수 있을 것 같음
        """
        combList = []
        def bt(comb, curMax):
            if len(comb) == k:
                # 목표 달성
                combList.append(comb)
            else:
                # recursion case -> 작은숫자부터 해보자
                for i in range(curMax+1, n+1):
                    # 가장 최근에 넣은 값이 가장 큰 값이 되도록 BT 확장
                    bt(comb+[i], i)
        bt([], 0)
        return combList