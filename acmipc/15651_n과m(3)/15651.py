import sys
input = sys.stdin.readline

# 1 <= m <= n <= 7
n,m = map(int, input().split())
nominate = [i for i in range(1,n+1)] # 1~n 까지
# 1~n에서 m개를 고른 수열을 순차적으로 출력
def BT(arr:list, level:int):
    # print(f'BT called!, arr : {arr}, level : {level}')
    if level == m:
        print(*arr)
    else:
        for num in nominate:
            # if num not in arr: -> n과m(1)에 들어가면 됨
            BT(arr+[num], level+1)

BT([],0)