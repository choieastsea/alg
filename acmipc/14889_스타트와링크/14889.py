import sys
input = sys.stdin.readline

def getScore(teams):
    global matrix
    score = 0
    for i in range(len(teams)):
        for j in range(i+1, len(teams)):
            a = teams[i]
            b = teams[j]
            score += (matrix[a][b] + matrix[b][a])
    return score

def getScoreDiff(A):
    # A팀 있을 때, B팀과의 점수 차이 계산
    B = [i for i in range(n) if i not in A]
    # print(A,B)
    # print(abs(getScore(A) - getScore(B)))
    return abs(getScore(A) - getScore(B))

def BT(selected, start):
    global visited
    global diff
    if  len(selected)== n//2: # n//2
        # BASIC CASE : score 계산
        # print(selected)
        curDiff = getScoreDiff(selected) # A팀과 B팀의 점수 차이 계산하여 결과에 추가
        if curDiff < diff:
            # diff가 최소를 유지하도록 update
            diff = curDiff
    else:
        # RECURSION CASE : search space 확장 및 탐색
        for i in range(start, len(visited)):
            if not visited[i]:
                visited[i] = True
                BT(selected + [i], i+1)
                visited[i] = False

def solution(matrix, n):
    A = [] # A팀
    BT(A, 0)
    return 0

if __name__ == "__main__":
    n = int(input())
    visited = [False for _ in range(n)]
    diff = 100*(n**2)
    matrix = [list(map(int, input().split())) for _ in range(n)]
    solution(matrix, n)
    print(diff)
    