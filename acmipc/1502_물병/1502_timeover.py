from sys import stdin
input = stdin.readline

def getCnt(water:int):
    # x개의 물병으로 합쳐서 남은 물병수를 구하는 함수
    # 2진수로 만든뒤 1의 갯수와 같다
    binary_water = bin(water)[2:]
    cnt = 0
    for ch in binary_water:
        if ch == '1':
            cnt += 1
    # print(cnt)
    return cnt

if __name__ == "__main__":
    n, k = map(int, input().split()) # n~10^7, k ~ 1000
    # greedy?
    for i in range(2**1001-1): # 범위 너무 큰가? ㅋ
        if getCnt(n+i) <=k:
            print(i)
            exit(0)
    print(-1)