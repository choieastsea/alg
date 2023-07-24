import sys
input = sys.stdin.readline
ZERO = 0

n = int(input()) # n*n sized matrix
dp = [[ZERO for _ in range(n+10)] for _ in range(n+10)] # dp[i][j]는 출발지부터 (i,j)까지의 경로의 수
arr = []
for _ in range(n):
    arr.append(list(map(int,input().split(' ')))) # 써있는 만큼만 아래 또는 오른쪽으로 이동 가능
dp[0][0] = 1

for i in range(n):
    for j in range(n):
        # arr를 탐색하면서, dp의 값들을 채워넣어주면 되지 않을까...
        moves = arr[i][j]
        if dp[i][j] != ZERO and moves != ZERO:
            # print(f'dp[{i}][{j}] : {dp[i][j]}')
            dp[i+moves][j] += dp[i][j]
            dp[i][j+moves] += dp[i][j]
        # print(f'i : {i}, j : {j}, moves : {moves}')
        # for x in range(n):
        #     for y in range(n):
        #         print(dp[x][y], end=' ')
        #     print()
        # print('==============================')
# for i in range(n):
    # for j in range(n):
    #     print(dp[i][j], end=' ')
    # print()

print(dp[n-1][n-1])