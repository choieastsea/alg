import sys
input = sys.stdin.readline

def isABiggerThanB(a,b):
    if a[0] > b[0] and a[1] > b[1]:
        return True
    return False

def solution(size_list, n):
    size_rank = [1 for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j:
                if isABiggerThanB(size_list[j], size_list[i]): # j덩치가 i보다 크다면 i의 rank 올리기
                    size_rank[i] += 1
    return size_rank

if __name__ == "__main__":
    n = int(input())
    size_list = []
    for _ in range(n):
        height, weight = map(int,input().strip().split(' '))
        size_list.append((weight,height))
    size_rank = solution(size_list, n)
    print(*size_rank)
