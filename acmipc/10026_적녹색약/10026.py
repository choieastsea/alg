from sys import stdin, setrecursionlimit
input = stdin.readline
setrecursionlimit(10**6)
n = int(input())
visited_normal, visited_unnormal = [[False for _ in range(n)]for _ in range(n)], [
    [False for _ in range(n)]for _ in range(n)]
board = [list(input().rstrip())for _ in range(n)]


def dfs(isNormal: bool, i: int, j: int):
    """
    isNormal이면, [i][j]와 같은 주변만 탐색
    not isNormal이면, R과 G는 같은 것으로 간주
    """
    if isNormal:
        visited_normal[i][j] = True
    else:
        visited_unnormal[i][j] = True
    for dr, dc in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        i_ = i + dr
        j_ = j + dc
        if i_ < n and i_ >= 0 and j_ < n and j_ >= 0:
            if (isNormal and not visited_normal[i_][j_] and board[i][j] == board[i_][j_]) or (not isNormal and not visited_unnormal[i_][j_] and (board[i][j]+board[i_][j_] in ['RR','GG','RG','GR'] or board[i][j] == board[i_][j_])):
                dfs(isNormal, i_, j_)


normal_cnt, unnormal_cnt = 0, 0
for i in range(n):
    for j in range(n):
        if not visited_normal[i][j]:
            dfs(True, i, j)
            normal_cnt += 1
        if not visited_unnormal[i][j]:
            dfs(False, i, j)
            unnormal_cnt += 1
print(normal_cnt, unnormal_cnt)
