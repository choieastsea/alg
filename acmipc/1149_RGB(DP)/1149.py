from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    R,G,B = 0,1,2
    costs = [list(map(int,input().split())) for _ in range(n)]
    dp = [[0,0,0] for _ in range(n)] # i번째 집을 r, g, b로 칠했을 때 최소 누적 비용
    dp[0] = costs[0]
    for i in range(1,n):
        dp[i][R] = min(dp[i-1][G], dp[i-1][B]) + costs[i][R]
        dp[i][G] = min(dp[i-1][R], dp[i-1][B]) + costs[i][G]
        dp[i][B] = min(dp[i-1][R], dp[i-1][G]) + costs[i][B]
    print(min(dp[n-1]))