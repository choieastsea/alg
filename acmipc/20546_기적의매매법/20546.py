# 33 매매법
# [준현] "BNP"
# greedy하게 최대한 삼

# [성민] "TIMING"
# 1. 3일 연속 가격 상승시 전량 매도
# 2. 3일 연속 가격 하락시 전량 매수

# 자산 = 현금 + 해당일의 주가 * 주식수
# 비긴 경우 "SAMESAME"

cash = int(input())
# 돈을 나눠준다
jh = {'cash' : cash, 'stock_count' : 0}
sm = {'cash' : cash, 'stock_count' : 0}
# 주가의 흐름
stock_chart = list(map(int, input().split()))

def greedy_buy(today_stock_price, buyer):
    changes = buyer['cash']
    count = changes // today_stock_price
    if count > 0:
        after_buy = changes % today_stock_price
        # print(f'after buy : {after_buy}, count : {count}')
        buyer['cash'] = after_buy
        buyer['stock_count'] += count

def greedy_sell(today_stock_price, buyer):
    count = buyer['stock_count']
    if count > 0:
        after_sell = buyer['cash'] + count*today_stock_price
        buyer['cash'] = after_sell
        buyer['stock_count'] = 0

uuu = 0 #연속 상승 카운트 
ddd = 0 #연속 하락 카운트
stock_yesterday = stock_chart[0]

for stock_today in stock_chart:
    #jh buy
    greedy_buy(stock_today, jh)
    #sm buy and sell
    if stock_yesterday < stock_today:
        uuu += 1
        ddd = 0
    elif stock_yesterday > stock_today:
        uuu = 0
        ddd += 1
    else:
        uuu = 0
        ddd = 0
    if uuu >= 3:
        # 전량 매도
        greedy_sell(stock_today, sm)
    elif ddd >= 3:
        # 전량 매수
        greedy_buy(stock_today, sm)
    stock_yesterday = stock_today

# 승리 판단
# print(jh)
# print(sm)
jh_total = jh['cash'] + jh['stock_count'] * stock_yesterday
sm_total = sm['cash'] + sm['stock_count'] * stock_yesterday
# print(f'jh : {jh_total}, sm : {sm_total}')
if jh_total > sm_total:
    print('BNP')
elif jh_total < sm_total:
    print('TIMING')
else:
    print('SAMESAME')