from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    wines = list(int(input())for _ in range(n))
    if n == 1:
        print(wines[0])
        exit(0)
    drinks = [[0,0] for _ in range(n)] # i번째 포도주까지 마셨을 때, 최대 마실 수 있는 양(3개 연속 선택 불가)
    drinks[0] = [0, wines[0]]
    drinks[1] = [wines[0], wines[0] + wines[1]] # i 안마셨을 때, i 마셨을 때
    for i in range(2,n):
        drinks[i][0] = max(drinks[i-1][0], drinks[i-1][1]) # 해당 wine 안마셨을 때,
        drinks[i][1] = max(drinks[i-1][0], drinks[i-2][1], drinks[i-2][0] + wines[i-1]) + wines[i]
    print(max(drinks[n-1]))