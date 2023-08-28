class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_size = len(matrix)
        col_size= len(matrix[0])
        strt = 0
        end = col_size * row_size - 1
        while strt <= end:
            mid = (strt+end) // 2
            row = mid // col_size
            col = mid % col_size
            # print(row, col, matrix[row][col])
            if matrix[row][col] > target:
                end = mid - 1
            elif matrix[row][col] < target:
                strt = mid + 1
            else:
                return True
        return False