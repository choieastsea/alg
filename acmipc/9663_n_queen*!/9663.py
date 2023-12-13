from sys import stdin
input = stdin.readline

n = int(input())
case = 0
not_col = [False for _ in range(n)]
not_upper = [False for _ in range(2*n)]
not_lower = [False for _ in range(2*n)]


def BT(row):
    """
    row 행에 퀸을 넣었을 때의 경우를 구함
    """
    global case
    if row == n:  # n-1 번째 row 까지 도달
        case += 1
        return
    for col in range(n):
        if not not_col[col] and not not_upper[row + col] and not not_lower[row - col]:
            # row, col에 queen이 가능함
            not_col[col] = True
            not_upper[row+col] = True
            not_lower[row-col] = True
            BT(row+1)  # 다음 행으로 넘어가서 실행
            not_col[col] = False
            not_upper[row+col] = False
            not_lower[row-col] = False

BT(0)
print(case)
