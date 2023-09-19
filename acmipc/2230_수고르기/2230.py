from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n, m = map(int, input().split())  # n ~ 100,000
    arr = list(int(input()) for _ in range(n))
    # n 개의 배열에서 차이가 m이상인 가장 작은 차이 -> 정렬하고 투포인터?
    arr.sort()
    left = 0
    right = 1
    minDiff = arr[n-1] - arr[0]
    while left <= n-1 and right <= n-1:
        diff = arr[right] - arr[left]
        if diff >= m:
            # 차이 줄이기 위해 left ++
            minDiff = min(minDiff, diff)
            left += 1
        else:
            # 차이 늘리기 위해 right ++
            right += 1
    print(minDiff)
