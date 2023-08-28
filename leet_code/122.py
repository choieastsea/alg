class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        주름을 펴서 최대의 이익
        일단 사고,
        오르면 팔고 다시 그 가격에 산다.
        떨어지면 그냥 그 가격에 산다(이전에 산 것은 무시)
        """
        buying_price = prices[0]
        profit = 0
        for price in prices:
            if buying_price < price: # 가격 오름
                profit += (price - buying_price) # 팔기
            buying_price = price # 내리거나 오르거나 일단 그 가격으로 산다고 가정함
        return profit