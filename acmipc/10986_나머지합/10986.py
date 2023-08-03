from sys import stdin
input = stdin.readline

def solution(S, m):
    # 기존 방식
    # for i in range(len(S)):
    #     for j in range(i+2, len(S)):
    #         if (S[j] - S[i]) % m == 0:
    #             cnt += 1
    # => 10^12는 너무 크므로 다른 방법 찾아야함
    """
    누적합 배열 S, 정수 m => m으로 나누어떨어지는 구간[i,j]의 갯수 (i<j인 경우...)
    S[i+1] : 0~i 까지 더한 걸 m으로 나눈 나머지
    S[i] == S[j]라면, (a[i] + ,,, + a[j-1]) % m == 0, 즉 [i,j]가 0으로 나누어 떨어진다
    """
    cnt = 0
    restCnt = [0 for _ in range(m)] # 나머지가 0~m-1 인 것들의 수
    for i in range(1, len(S)):  # 10^12 => too much...
        restCnt[S[i]] += 1
    cnt += restCnt[0] # 나머지가 0인 것들 그 자체로 더하기
    for rest in restCnt:
        cnt += rest*(rest-1)//2 # [3, 2, 1] => 나머지가 같은 것들끼리 구간을 만든다 => combination으로 2개 뽑으면 됨
    return cnt

if __name__ == "__main__":
    n,m = map(int, input().split()) # 1 ≤ N ≤ 10^6, 2 ≤ M ≤ 10^3
    # 연속된 구간의 합이 m으로 나누어 떨어지는 구간의 갯수 구하기 => 합이 나누어 떨어지면, 나머지의 합도 나누어 떨어질 것
    arr = list(map(int, input().split()))
    S = [0 for _ in range(n+1)] # S[i] : arr[0]~arr[i-1]까지 더한값을 m으로 나눈 나머지
    for i in range(len(arr)):
        S[i+1] = (S[i] + arr[i]) % m
    cnt = solution(S,m)
    print(cnt)
    