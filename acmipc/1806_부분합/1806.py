from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    """
    부분합이 S이상이 되는 것 중 가장 짧은 것의 길이를 출력
    -> 자연수 배열이므로 누적합 S 이상인 것 구하고, 거기서부터 앞부분 줄이면 될듯?
    """
    N, S = map(int, input().split())
    a = list(map(int, input().split()))
    min_length = 100001
    strt = 0
    acc_sum = 0
    for end in range(len(a)):
        acc_sum += a[end]
        if acc_sum >= S:
            # strt 줄이기
            while True:
                if strt <= len(a) - 1 and acc_sum - a[strt] >= S:
                    acc_sum -= a[strt]
                    strt += 1
                else:
                    min_length = min(min_length, end-strt + 1)
                    break
    print(min_length if min_length != 100001 else 0)
