from sys import stdin
input = stdin.readline

def bt(num_string):
    """
    level조건 없이 다른 조건(감소하는 수)으로만 가는 BackTracking
    """
    global resultSet
    if num_string != '':
        resultSet.add(int(num_string))
    for i in range(0,10):
        # 줄어드는 수의 경우(현재의 마지막보다 작은 숫자), 0~9를 붙이고 다음으로
        if num_string == '' or int(num_string[-1]) > i:
            bt(num_string+f'{i}')

if __name__ =="__main__":
    n = int(input()) # n ~ 1,000,000
    # BackTracking으로 줄어드는 숫자들의 배열 만들기
    resultSet = set()
    bt('')
    sortedResult = sorted(list(resultSet))
    if len(sortedResult) >= n:
        print(sortedResult[n-1])
    else:
        print(-1)