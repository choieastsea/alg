N,M,R = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int,input().split()))[:])

def print_matrix(A):
    for row in A:
        for el in row:
            print(el,end=" ")
        print()

def rotate_kth_layer(k):
    '''
    A 배열의 바깥쪽(0)부터 k번째 층을 회전시킨다
    '''
    row_count = N - 2*k #k부터 row_count만큼 영역임
    col_count = M - 2*k #k부터 col_count만큼 영역임
    if row_count <=0 or col_count <=0:
        return
    else:
        # print(f'k : {k}) row : {row_count}, col : {col_count}')
        #회전시킴
        row_end = k + row_count - 1
        col_end = k + col_count - 1
        row_start = k
        col_start = k
        # 1번방향(왼쪽)
        tmp_1 = A[row_end][col_start]
        for i in range(row_end, row_start ,-1):
            # print(f"A[{i}][{col_start}] = A[{i-1}][{col_start}]({A[i-1][col_start]})")
            A[i][col_start] = A[i-1][col_start]
        # 2번방향(아래)
        tmp_2 = A[row_end][col_end]
        for j in range(col_end,col_start +1 ,-1):
            # print(f"A[{row_end}][{j}] = A[{row_end}][{j-1}]({A[row_end][j-1]})")
            A[row_end][j] = A[row_end][j-1]
        A[row_end][col_start+1] = tmp_1
        # print(f"A[{row_end}][{col_start+1}] = {tmp_1}")
        # 3번방향(오른쪽)
        tmp_3 = A[row_start][col_end]
        for i in range(row_start,row_end -1):
            # print(f"A[{i}][{col_end}] = A[{i+1}][{col_end}]({A[i+1][col_end]})")
            A[i][col_end] = A[i+1][col_end]
        A[row_end-1][col_end] = tmp_2
        # print(f"A[{row_end-1}][{col_end}] = {tmp_2}")
        # 4번방향(위쪽)
        tmp_4 = A[row_start][col_start]
        for j in range(col_start, col_end-1 ):
            # print(f"A[{row_start}][{j}] = A[{row_start}][{j+1}]({A[row_start][j+1]})")
            A[row_start][j] = A[row_start][j+1]
        A[row_start][col_end - 1] = tmp_3
        #다음 층으로 넘어감
        rotate_kth_layer(k+1)

for _ in range(R):
    # R에 대한 최적화가 필요해보이지만...
    rotate_kth_layer(0)
print_matrix(A)