import sys
input = sys.stdin.readline

"""
    연산 1 : 가 3으로 나누어 떨어지면, 3으로 나눈다.
    연산 2 : X가 2로 나누어 떨어지면, 2로 나눈다.
    연산 3 : 1을 뺀다.
    n 입력 들어왔을때, 1을 만들기까지 사용하는 최소한의 연산수
    bottom up으로 생각했을 때, greedy는 불가능 (200-400-800-801 << 200-600-...-801)
    -> DP!
"""

if __name__ == "__main__":
    n = int(input())
    DP = [1000000 for _ in range(n+1)] # DP[n] : n을 만들기 위해 필요한 최소의 연산수
    DP[0] = 0
    DP[1] = 0
    for i in range(1, n+1):
        if i + 1 <= n:
            DP[i+1] = min(DP[i+1], DP[i] + 1)
        if i * 2 <= n:
            DP[i*2] = min(DP[i*2], DP[i] + 1)
        if i * 3 <= n:
            DP[i*3] = min(DP[i*3], DP[i] + 1)
    # print(DP)
    print(DP[n])
