from collections import deque

def rotate(matrix, row_size, query):
    """
    시계방향으로 query 만큼의 가장자리 회전, 
    가장 작은 숫자를 리턴
    """
    lr, lc, rr, rc = query # 좌상단 ~ 우하단
    lr -= 1
    lc -= 1
    rr -= 1 
    rc -= 1
    min_num = 10000
    index_list = []
    # 좌상단부터 시계방향으로 인덱스들을 저장
    # 상단
    for i in range(lc, rc):
        index_list.append((lr,i))
    # 우측
    for i in range(lr, rr):
        index_list.append((i,rc))
    # 하단
    for i in range(rc, lc, -1):
        index_list.append((rr,i))
    # 좌측
    for i in range(rr, lr, -1):
        index_list.append((i,lc))
    q = deque()
    for row, col in index_list:
        q.append(matrix[row*row_size+col])
    # 1회 회전
    q.appendleft(q.pop())
    # matrix 재할당
    for i, (row,col) in enumerate(index_list):
        matrix[row*row_size+col] = q[i]
        if min_num > q[i]:
            min_num = q[i]
    return min_num
    
    
def solution(rows, columns, queries):
    answer = []
    matrix = [i+1 for i in range(rows*columns)]
    for query in queries:
        answer.append(rotate(matrix, columns, query))
    return answer

print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))    #[8, 10, 25]
print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))  #[1, 1, 5, 3]
print(solution(100,	97,	[[1,1,100,97]]))    #[1]