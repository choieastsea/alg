from sys import stdin
input = stdin.readline

n = int(input())
line = list(map(int, input().split()))
maxdp, mindp = [line[:], [0, 0, 0]], [line[:], [0, 0, 0]]
prev, cur = 0, 0
for i in range(1, n):
    line = list(map(int, input().split()))
    # 다음 행의 값은 이전 행의 열과 같거나 이웃한 것만 가능
    if i % 2 == 0:
        prev = 1
        cur = 0
    else:
        prev = 0
        cur = 1
    maxdp[cur][0] = max(maxdp[prev][0], maxdp[prev][1]) + line[0]
    maxdp[cur][1] = max(maxdp[prev][0], maxdp[prev][1],
                        maxdp[prev][2]) + line[1]
    maxdp[cur][2] = max(maxdp[prev][1], maxdp[prev][2]) + line[2]

    mindp[cur][0] = min(mindp[prev][0], mindp[prev][1]) + line[0]
    mindp[cur][1] = min(mindp[prev][0], mindp[prev][1],
                        mindp[prev][2]) + line[1]
    mindp[cur][2] = min(mindp[prev][1], mindp[prev][2]) + line[2]
print(max(maxdp[cur]), min(mindp[cur]))
