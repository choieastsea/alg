class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[]for _ in range(numRows)]
        rowIdx = 0
        isRowIncrease = True
        for ch in s:
            # 문자 하나씩 해당하는 row의 matrix에 추가
            matrix[rowIdx].append(ch)
            if isRowIncrease:
                if rowIdx < numRows - 1:
                    rowIdx += 1
                else:
                    isRowIncrease = False
                    rowIdx -= 1
            else:
                if rowIdx > 0:
                    rowIdx -= 1
                else:
                    isRowIncrease = True
                    rowIdx += 1
        newS = ''
        for row in matrix:
            newS += ''.join(row)
        return newS