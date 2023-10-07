from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split())
    coin_value = [int(input()) for _ in range(n)]
    D = [0 for _ in range(k+1)] # D[i] : 가치의 합이 i가 되는 경우
    D[0] = 1 # 0원은 한가지
    for i in range(1,n+1):
        # i 번째 동전까지 사용했을 때,
        for j in range(coin_value[i-1], k+1):
            # 기존 j원의 경우의 수 + i번째 동전 포함된 경우의 수 -> 모든 동전에 대하여 경우의 수 구하면 됨
            D[j] = D[j] + D[j-coin_value[i-1]]
    print(D[-1])