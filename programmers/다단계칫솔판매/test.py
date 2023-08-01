class SalesMan:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.totalAmount = 0
    def __str__(self):
        return f'{self.totalAmount}'

def money(salesMan, amount):
    """
    salesMan이 amount 만큼 벌었을 때, 자신과 부모에게 분배
    """
    # print(f'money({salesMan.name}, {amount})')
    forParent = int(amount*0.1)
    forMe = amount - forParent
    if salesMan.parent is None:
        # basic case
        salesMan.totalAmount += forMe
        return
    else:
        # recursion case
        salesMan.totalAmount += forMe
        # print(forParent, forMe)
        if forParent > 0:
            money(salesMan.parent, forParent)
        
def solution(enroll, referral, seller, amount):
    answer = []
    enrollDict = {}
    for i, member in enumerate(enroll):
        enrollDict[member] = SalesMan(member)
        parent = referral[i]
        if parent != "-":
            # 부모 등록
            enrollDict[member].parent = enrollDict[parent]
    for i, sell in enumerate(seller):
        money(enrollDict[sell],amount[i]*100)
    for key, value in enrollDict.items():
        answer.append(value.totalAmount)
    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10])) # [360, 958, 108, 0, 450, 18, 180, 1080])
print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],	["sam", "emily", "jaimie", "edward"],[2, 3, 5, 4])) # [0, 110, 378, 180, 270, 450, 0, 0]