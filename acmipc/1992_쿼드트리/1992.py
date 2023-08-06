from sys import stdin
input = stdin.readline

def makePart(matrix):
    """
    matrix를 4개로 나눈다
    """
    n = len(matrix)
    part_size = n//2
    part = [[],[],[],[]]    
    for i, line in enumerate(matrix):
        if i < part_size:
            part[0].append(line[:part_size])
            part[1].append(line[part_size:])
        else:
            part[2].append(line[:part_size])
            part[3].append(line[part_size:])
    return part

def compress(matrix):
    """
    n*n의 matrix를 4분할
    4분할 된 부분이 같은 수를 리턴한다면 하나로 묶어준다.!
    """
    n = len(matrix)
    sumOfMatrix = 0
    for line in matrix:
        sumOfMatrix += sum(line)

    if sumOfMatrix == n*n: # 1로 가득참
        return 1
    elif sumOfMatrix == 0: # 0으로 가득참
        return 0
    else: 
        # recursion case
        # partition 나눠서 실행
        part1, part2, part3, part4 = makePart(matrix)
        return f'({compress(part1)}{compress(part2)}{compress(part3)}{compress(part4)})'
    
if __name__ == "__main__":
    n = int(input()) # n : 2의 거듭제곱
    matrix = [list(map(int,input().strip())) for _ in range(n)]
    print(compress(matrix))