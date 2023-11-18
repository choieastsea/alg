T = int(input())
  
  
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
def buyAndSell(strt, end, max_idx):
    """
    strt ~ end 범위에서 maxInd에 최대값 있을 때, 그 전까진 사고 maxInd에서 판매
    maxInd ~ end까지 최댓값으로 재귀
    """
    global stocks_input
    if strt >= end:
        return 0
    profit = 0
    max_price = stocks_input[max_idx]
    for i in range(strt, max_idx):
        # max 까지 누적 이익을 더함
        profit += (max_price-stocks_input[i])
    next_max_idx = max_idx+1
    for i in range(max_idx+1, end+1):
        if stocks_input[next_max_idx] < stocks_input[i]:
            next_max_idx = i
    rest_profit = buyAndSell(max_idx+1, end, next_max_idx)
    # print(f'buyAndSell({strt},{end},{max_idx}), prev_profit : {profit}, rest_profit : {rest_profit}')
    return profit + rest_profit
  
  
def solution(days, stocks):
    """
    하루에 하나만 살 수 있음 (파는 건 자유)
    이때 최대의 이익 리턴
    -> "현재 구간에서 최댓값 이전은 다 사고, 최댓값에서 판매" 를 재귀적으로 수행
    """
    strt = 0
    profit = 0
    while strt < days:
        max_price = max(stocks[strt:days+1])
        max_idx = stocks[strt:days+1].index(max_price) + strt
        for i in range(strt, max_idx):
            # max 까지 누적 이익을 더함
            profit += (max_price - stocks[i])
        # max 오른쪽 구간에서 다음 루프 수행
        strt = max_idx + 1
  
    return profit
  
  
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    days_input = int(input())
    stocks_input = list(map(int, input().split()))
    print(f"#{test_case} {solution(days_input-1, stocks_input)}")
    # ///////////////////////////////////////////////////////////////////////////////////