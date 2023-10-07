from sys import stdin
input = stdin.readline

n, k = map(int, input().split())
wv = [tuple(map(int, input().split())) for _ in range(n)] # (weight, value)
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
# dp[i][j] : i번 물건까지 있다고 할 때, 총무게가 j 이하일 때, 가치의 최대 값
for i in range(1, n+1):
    for j in range(k+1):
        # i번째 무게(wv[i][0])가 들어올 수 있는 무게 한계인 경우
        if j >= wv[i-1][0]:
            # 선택하지 않거나(이전과 가치 동일), 선택하거나(이전가치 + 현재 물건의 가치)
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-wv[i-1][0]] + wv[i-1][1])
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j])
print(dp[n][k])