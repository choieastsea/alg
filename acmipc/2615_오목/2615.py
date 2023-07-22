import sys
input = sys.stdin.readline
N = 19
FIVE = 5
BLACK = '1'
WHITE = '2'

class Node:
    def __init__(self) -> None:
        self.color  = 0
        self.combo1 = 0
        self.combo2 = 0
        self.combo3 = 0
        self.combo4 = 0
    def __init__(self, color) -> None:
        self.color = color
        self.combo1 = 1
        self.combo2 = 1
        self.combo3 = 1
        self.combo4 = 1
    def __str__(self) -> str:
        # return f'[{self.combo1}/{self.combo2}/{self.combo3}]'
        return f'{max(self.combo1, self.combo2, self.combo3, self.combo4)}'

if __name__ == '__main__':
    matrix = [list(input().strip().split(' ')) for _ in range(N)]
    combo_matrix = [[None for _ in range(N)]for _ in range(N)]
    for i, line in enumerate(matrix):
        for j, str in enumerate(line):
            combo_matrix[i][j] = Node(str)
            if str == BLACK or str == WHITE: # black
                # check combo1
                if j > 0 and combo_matrix[i][j-1].color == str:
                    combo_matrix[i][j].combo1 = combo_matrix[i][j-1].combo1 + 1
                    if combo_matrix[i][j].combo1 == FIVE:
                        # 육목 거르기
                        if not (j < N-1 and matrix[i][j+1] == str):
                            print(f'{str}\n{i+1} {j-3}')
                            exit(0)
                # check combo2
                if i > 0 and combo_matrix[i-1][j].color == str:
                    combo_matrix[i][j].combo2 = combo_matrix[i-1][j].combo2 + 1
                    if combo_matrix[i][j].combo2 == FIVE:
                        # 육목 거르기
                        if not (i < N-1 and matrix[i+1][j] == str):
                            print(f'{str}\n{i-3} {j+1}')
                            exit(0)
                # check combo3
                if i > 0 and j > 0 and combo_matrix[i-1][j-1].color == str:
                    combo_matrix[i][j].combo3 = combo_matrix[i-1][j-1].combo3 + 1
                    if combo_matrix[i][j].combo3 == FIVE:
                        # 육목 거르기
                        if not (i < N-1 and j < N-1 and matrix[i+1][j+1] == str):
                            print(f'{str}\n{i-3} {j-3}')
                            exit(0)
                # check combo4
                if i > 0 and j < N-1 and combo_matrix[i-1][j+1].color == str:
                    combo_matrix[i][j].combo4 = combo_matrix[i-1][j+1].combo4 + 1
                    if combo_matrix[i][j].combo4 == FIVE:
                        # 육목 거르기
                        if not (i < N-1 and j > 0 and matrix[i+1][j-1] == str):
                            print(f'{str}\n{i+1} {j+1}')
                            exit(0)
            else:
                pass
    # for row in combo_matrix:
    #     for el in row:
    #         print(el, end=' ')
    #     print()
    print(0)

# 52퍼까진 가네...