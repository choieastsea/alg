from sys import stdin
input = stdin.readline

# 1912 후속 문제
INIT = -1000*100000
if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    DP = [[INIT,INIT] for _ in range(n)] # DP[i][0] : 아직 제외 안한 경우, DP[i][0] : 하나 제외 한 경우의 i까지의 합 최대
    # 제외는 최대 하나만 가능함 ... 적어도 하나는 선택해야함
    DP[0] = [arr[0], INIT]
    for i in range(1,n):
        DP[i][0] = max(DP[i-1][0]+arr[i], arr[i])
        DP[i][1] = max(DP[i-1][1]+arr[i], DP[i-1][0]) # i포함 안한 경우(DP[i-1]][0])와 이미 제거한 것에서 i포함한 경우
    # max in DP
    max_sum = INIT
    for row in DP:
        max_sum = max(max_sum, max(row))
    print(max_sum)
    