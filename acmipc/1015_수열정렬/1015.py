from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    p = sorted([(el, idx) for idx, el in enumerate(a)], key=lambda x: x[0])
    rank = [0 for _ in range(n)]
    # print(p)
    for i in range(n):
        rank[p[i][1]] = i
    print(*rank)
