class EmoticonDcInfo:
    def __init__(self, id, original_cost, dc_percent):
        self.id = id
        self.original_cost = original_cost
        self.dc_percent = dc_percent

    def getDcPrice(self):
        """
        original : 0~
        dc_percent : 10~40    
        """
        return int(self.original_cost*(100-self.dc_percent)/100)
    
    def __str__(self) -> str:
        return f'{self.id}) {self.original_cost} ({self.dc_percent}% sales)\n'
    
class UserSaleInfo:
    def __init__(self, id, std_percent, std_price, emoticons, totalPrice, isPlus):
        self.id = id
        self.std_percent = std_percent  # 이모티콘 구매 기준 퍼센트
        self.std_price= std_price       # 플러스 구매 기준 가격
        self.emoticons = emoticons
        self.totalPrice = totalPrice
        self.isPlus = isPlus

    def buyEmoticons(self, emoticons: list[EmoticonDcInfo]):
        for emoticon in emoticons:
            # print(self.std_percent, emoticon.dc_percent)
            if self.std_percent <= emoticon.dc_percent:
                # 기준 이상이면 이모티콘 일단 구매
                self.emoticons.append(emoticon)
                self.totalPrice += emoticon.getDcPrice()
                if self.totalPrice >= self.std_price:
                    self.isPlus = True

    def reset(self):
        """
        이모티콘 구매 기록 삭제
        """
        self.emoticons = []
        self.totalPrice = 0
        self.isPlus = False

    def __str__(self) -> str:
        return f'{self.id}) {self.emoticons} ({self.isPlus})\n'
    
def makeCases(limit, dc_percent_list, cases, total_cases):
    """
    emoticon이 limit개 있을 때, 세일할 수 있는 순열을 만든다
    [10,10,10] ~ [40,40,40] 
    """
    n = len(cases)
    if n == limit:
        total_cases.append(cases)
        return
    else:
        for percent in dc_percent_list:
            makeCases(limit, dc_percent_list, cases + [percent], total_cases)


def solution(users, emoticons):
    """
    input: user[i]=[할인기준%, 기준가격]의 배열 // emoticons[i]=i+1번 이모티콘의 정가
    output: 최대 목표 달성(가입자수 >> 판매액)시, ['이모티콘 플러스 가입자 수', '이모티콘 매출액']을 리턴
    """
    dc_percent_list = [10, 20, 30, 40]
    emoticon_dc_list = [EmoticonDcInfo(i+1, emoticons[i], 0) for i in range(len(emoticons))]
    user_sales_list = [UserSaleInfo(i+1, users[i][0], users[i][1], [], 0, False) for i in range(len(users))]
    # emoticon 할인할 수 있는 경우의 수
    dc_case_list = [] # [10,10,20,20] 등이 리스트로 존재
    makeCases(len(emoticons),dc_percent_list, [], dc_case_list)
    # print(dc_case_list)
    best_case = (0,0)
    for i, dc_case in enumerate(dc_case_list):
        for j, dc_percent in enumerate(dc_case):
            emoticon_dc_list[j].dc_percent = dc_percent
        # 이모티콘 dc percent 초기화 -> 케이스별로 사용자의 구매 여부 확인
        case_subscribers = 0
        case_sales = 0
        for k, user_sale in enumerate(user_sales_list):
            user_sale.buyEmoticons(emoticon_dc_list)
            if user_sale.isPlus:
                case_subscribers += 1
            else:
                case_sales += user_sale.totalPrice
            user_sale.reset()
        if best_case[0] < case_subscribers:
            best_case = (case_subscribers, case_sales)
        elif best_case[0] == case_subscribers:
            best_case = (case_subscribers, max(case_sales, best_case[1]))

    return best_case


if __name__ == "__main__":
    users = [[40, 10000], [25, 10000]]	
    emoticons = [7000, 9000]
    # print(solution(users, emoticons))

    users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]
    emoticons = [1300, 1500, 1600, 4900]
    print(solution(users, emoticons))