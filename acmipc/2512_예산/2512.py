from sys import stdin
input = stdin.readline

def calcBudgetSum(maxBudget):
    """
    상한선이 정해졌을 때, 줄 수 있는 예산의 합
    """
    global requestBudgetList
    budgetSum = 0
    for requestBudget in requestBudgetList:
        if requestBudget >= maxBudget:
            budgetSum += maxBudget
        else:
            budgetSum += requestBudget
    return budgetSum
    

def getMaximumBudget(budgetList, totalBudget):
    """
    totalBudget 이하의 최대의 budget의 합을 리턴
    상한선을 k라고 했을 때, 총 예산 g(k)는 증가함수 -> Binary Search
    g(k) <= totalBudget 인 k의 최댓값을 리턴
    """
    strt = 1 # budget : 1~100,000
    end = max(budgetList) # O(n)
    while strt <= end:
        mid = (strt + end) // 2
        budgetSum = calcBudgetSum(mid)
        # print(f'{strt}~{end}, mid : {mid}, budgetSum : {budgetSum}, totalBudget: {totalBudget}')
        if budgetSum <= totalBudget:
            # totalBudget 이하인 경우, 오른쪽으로 옮기기
            strt = mid + 1
        else:
            # 초과인 경우, 왼쪽으로 옮기기
            end = mid - 1
    return strt - 1
    

if __name__ == "__main__":
    n = int(input())
    requestBudgetList = list(map(int, input().split()))
    totalBudget = int(input()) # 1 ~ 1,000,000,000
    print(getMaximumBudget(requestBudgetList, totalBudget))
