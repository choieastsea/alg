class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 1. 한 행에 1-9 하나씩 있어야함
        # 2. 한 열에 1-9 하나씩 있어야함
        # 3. 3*3 블럭에 1-9 하나씩 있어야함
        NUM = 9
        row_set = set()
        col_set = set()
        block_set = set()
        
        for i in range(NUM):
            for j in range(NUM):
                element = board[i][j]
                if element != '.':
                    if (i,element) in row_set or (j,element) in col_set or (i//3,j//3,element) in block_set:
                        return False
                    row_set.add((i,element))
                    col_set.add((j,element))
                    block_set.add((i//3,j//3,element))
        return True