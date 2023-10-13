from sys import stdin

input = stdin.readline

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
alphabet = set(board[0][0])
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_cnt = 0


def bt(cur_row, cur_col, cnt):
    """
    cur_loc까지 alphabet들 방문했을 때, 더 이상 갈 수 없거나 마지막 도달하면 alphabet의 갯수를 기록한다
    """
    global max_cnt
    # print(f'bt called, cur : {cur_loc}, max_cnt : {max_cnt}, alphabet set : {alphabet}')
    max_cnt = max(max_cnt, cnt)
    for dr, dc in directions:
        next_row = cur_row + dr
        next_col = cur_col + dc
        if 0 <= next_row < r and 0 <= next_col < c and board[next_row][next_col]:
            if not board[next_row][next_col] in alphabet:
                alphabet.add(board[next_row][next_col])
                bt(next_row, next_col, cnt+1)
                alphabet.remove(board[next_row][next_col])


bt(0, 0, 1)
print(max_cnt)
