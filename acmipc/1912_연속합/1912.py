from sys import stdin
input = stdin.readline

INIT = -1000*100000

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    DP = [INIT for _ in range(n)] # DP[i] : x~i까지 더할때의 최댓값 (x는 모르지만)
    DP[0] = arr[0]
    for i in range(1, n):
        DP[i] = max(DP[i-1]+arr[i], arr[i]) # 이전 것의 누적값과 처음부터 시작할지
    # print(DP)
    print(max(DP))
