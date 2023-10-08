# n자리의 계단수의 갯수 를 1,000,000,000 으로 나눈 나머지 출력
# dp[n] = dp[n-1][0] + dp[n-1][1]*2 + ... + dp[n-1][9]

from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    dp = [[0 for _ in range(10)]for _ in range(n)]
    dp[0] = [1 for _ in range(10)]
    dp[0][0] = 0
    for i in range(1, n):
        for j in range(10):
            if j != 0 and j!= 9:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            elif j == 0:
                dp[i][j] = dp[i-1][1]
            else:
                dp[i][j] = dp[i-1][8]
    print(sum(dp[n-1])%1000000000)