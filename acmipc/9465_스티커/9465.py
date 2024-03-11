from sys import stdin
input = stdin.readline
UP, DOWN = 0, 1
T = int(input())
for _ in range(T):
    n = int(input())
    sticker = [list(map(int, input().split())) for _ in range(2)]
    # dp[i][j] : 왼쪽부터해서 i,j-1 번째 스티커를 뗐을 때, 최대 점수의 합
    dp = [[0 for _ in range(n+1)]for _ in range(2)]
    dp[UP][1], dp[DOWN][1] = sticker[UP][0], sticker[DOWN][0]
    if n > 1:
        for i in range(2, n+1):
            # 현재칸 : max(이전꺼에서 반대 누적값 , 이전꺼의 그 전꺼의 반대 누적값) + 현재칸
            dp[UP][i] = max(dp[DOWN][i-1], dp[DOWN][i-2]) + sticker[UP][i-1]
            dp[DOWN][i] = max(dp[UP][i-1], dp[UP][i-2]) + sticker[DOWN][i-1]
    print(max(dp[UP][n], dp[DOWN][n]))