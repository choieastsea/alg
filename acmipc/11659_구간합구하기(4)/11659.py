import sys
input = sys.stdin.readline

if __name__ == "__main__":
    n, m = list(map(int, input().split(' ')))
    S = [0 for _ in range(n+1)]
    A = list(map(int, input().split(' ')))
    for i in range(len(A)):
        S[i+1] = S[i] + A[i]
    for _ in range(m):
        i, j = list(map(int, input().split(' ')))
        print(S[j]-S[i-1])