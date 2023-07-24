import sys 
input = sys.stdin.readline
BLANK = 10
n = int(input())
# 더해서 n이 되는 조합을 찾는다. 4개 이하로 표현해야함
dp = [BLANK for _ in range(n+1)] # dp[i]는 더해서 i가 되는 제곱수들의 합으로 표현했을 때, 그 수의 최솟값
def check_is_square(n):
    if n <0:
        return False
    return n**(1/2) % 1 == 0

def lagrange(n):
    dp[1] = 1
    for i in range(2,n+1):
        if dp[i] == BLANK:
            #i가 제곱수인 경우
            if check_is_square(i):
                dp[i] = 1
            else:
                # 여러개의 제곱수의 합으로 표현 가능한 경우
                i_root_ = int(i**(1/2))
                for j in range(i_root_, 0, -1):
                    remain = i - j**2
                    if dp[remain] != BLANK:
                        dp[i] = min(dp[i],1 + dp[remain])
    return dp[n]

print(lagrange(n))
