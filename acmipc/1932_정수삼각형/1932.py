from sys import stdin
input = stdin.readline

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]
for level, line in enumerate(triangle):
    if level > 0:
        for i in range(len(line)):
            if i == 0:
                line[i] += prev_line[0]
            elif i == len(line)-1:
                line[i] += prev_line[i-1]
            else:
                # 윗줄에서 더 큰것과 더하면 된다
                line[i] += max(prev_line[i-1],prev_line[i])
    prev_line = line
print(max(triangle[-1]))