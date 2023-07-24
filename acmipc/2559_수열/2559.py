import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    temperature = list(map(int, input().split(' ')))
    S = [0 for _ in range(n+1)] # S[n] : sum of a[0]~a[n-1]
    # init S
    for i in range(n):
        S[i+1] = S[i] + temperature[i]
    # get max sum of sequence of temperature during k days..
    maxSumDuringK = -10000000 # -10~10도 100000일

    for i in range(0, n-k+1):
        sumDuringK = S[i+k] - S[i] # i~i+k-1 일 까지의 합
        if sumDuringK > maxSumDuringK:
            maxSumDuringK = sumDuringK
    print(maxSumDuringK)