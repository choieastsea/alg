from sys import stdin
input = stdin.readline

def z(row, col, n):
    """
    2^n * 2^n 배열에서 Z방식으로 방문할때, (row, col)는 몇번째인지
    """
    # print(f'z({row},{col},{n})')
    if n == 1:
        basic_index = [[0,1],[2,3]] # n=1
        return basic_index[row][col]
    else:
        # recursion case
        beforeSize = 2**(n-1)
        blockSize = 4**(n-1)
        # print(f'{beforeSize}에서 ({row%beforeSize},{col%beforeSize}) 언제? + ({row//beforeSize}, {col//beforeSize})사분면{((row//beforeSize) * 2 + col//beforeSize)*blockSize}')
        return z(row%beforeSize,col%beforeSize, n-1) + ((row//beforeSize) * 2 + col//beforeSize)*blockSize

if __name__ == "__main__":
    N, r, c = map(int, input().split()) # 2^N 크기의 matrix를 z로 탐색했을 때, (r,c)는 언제 방문하는지
    print(z(r,c,N))
    