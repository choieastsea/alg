import sys
input = sys.stdin.readline

def str_to_pos(str):
    alp = str[0]
    if alp == 'A':
        col = 0
    elif alp == 'B':
        col = 1
    elif alp == 'C':
        col = 2
    elif alp == 'D':
        col = 3
    elif alp == 'E':
        col = 4
    elif alp == 'F':
        col = 5
    elif alp == 'G':
        col = 6
    elif alp == 'H':
        col = 7
    else:
        ValueError('col error')
    row = 8 - int(str[1])
    return row,col

def move_to_pos(str):
    if str == 'R':
        row,col = 0,1
    elif str == 'L':
        row,col = 0,-1
    elif str == 'B':
        row,col = 1,0
    elif str == 'T':
        row,col = -1,0
    elif str == 'RB':
        row,col = 1,1
    elif str == 'RT':
        row,col = -1,1
    elif str == 'LB':
        row,col = 1,-1
    elif str == 'LT':
        row,col = -1,-1
    else:
        ValueError('move error')
    return row,col

def pos_to_str(pos):
    row_n, col_n = pos
    if col_n == 0:
        col = 'A'
    elif col_n == 1:
        col = 'B'
    elif col_n == 2:
        col = 'C'
    elif col_n == 3:
        col = 'D'
    elif col_n == 4:
        col = 'E'
    elif col_n == 5:
        col = 'F'
    elif col_n == 6:
        col = 'G'
    elif col_n == 7:
        col = 'H'
    return f'{col}{8-row_n}'
    
    
def pos_after_move(king, stone, move):
    move_row, move_col = move
    king_row, king_col = king
    stone_row, stone_col = stone
    
    # king 이동시키기
    king_row_after = king_row + move_row
    king_col_after = king_col + move_col

    if king_row_after >= 0 and king_row_after < 8 and king_col_after >= 0 and king_col_after < 8:
        # king 이동 가능한 경우
        king = king_row_after, king_col_after
        # stone과 겹치는지 확인
        if stone == king:
            # print('겹칠거 같아요')
            stone_row_after= stone_row + move_row
            stone_col_after = stone_col + move_col
            if stone_row_after >= 0 and stone_row_after < 8 and stone_col_after >= 0 and stone_col_after < 8:
                stone = stone_row_after, stone_col_after
            else:
                # stone도 나가게 되는 경우, king roll back
                king = (king_row, king_col)
    return king, stone

if __name__ == "__main__":
    king_str, stone_str, n = input().split(' ')
    king = str_to_pos(king_str)
    stone = str_to_pos(stone_str)
    for _ in range(int(n)):
        move = move_to_pos(input().strip())
        king, stone = pos_after_move(king, stone, move)
    print(pos_to_str(king))
    print(pos_to_str(stone))