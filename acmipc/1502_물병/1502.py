from sys import stdin
input= stdin.readline

def countOne(binary:str):
    cnt = 0
    for ch in binary:
        cnt += 1 if ch == '1' else 0
    return cnt

if __name__ == "__main__":
    """
    greedy하게 보면, n 이상이면서, n+a를 이진수로 표현했을 때, 1의 갯수가 k개 이하가 되도록하는 a의 최솟값을 찾으면 된다
    """
    n, k = map(int, input().split()) # n~10^7, k ~ 1000
    # k 번째까지 복사하고 1 더해주면 될듯? 그 뒤는 0으로...
    binary_n = bin(n)[2:] # 4 -> '100' 2진수 변환
    totalCnt = countOne(binary_n)
    # print(binary_n)
    if totalCnt <= k:
        # 이미 만족하는 경우 더할 필요 없음
        print(0)
    else:
        cnt1 = 0 # 앞에서부터의 1의 갯수
        binary_target = '0'
        for i, ch in enumerate(binary_n):
        # k번째까지 복사함
            if ch == '1':
                cnt1 += 1
                if cnt1 == k:
                    binary_target += binary_n[:i]
                    break
        # print(binary_target)
        # 1 더하고 0 붙히기
        target = (int(binary_target,2) + 1) * (2**(len(binary_n)-len(binary_target)+1))
        binary_target = bin(target)[2:]
        # print(binary_target)
        print(target-n)
    # n=101001100(332) & k=3 -> 101010000
    # n=10101100(172) & k=3 -> 10110000
    # n=1111 & k=3 -> 10000
