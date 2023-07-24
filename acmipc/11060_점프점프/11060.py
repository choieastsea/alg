# 1*N 사이즈 배열
# k번째 칸의 값을 Ak라 할때, i번 칸 다음에는 i+1~i+Ai번째 칸 중에 갈 수 있음
# 시작부터 끝까지 최소 몇번의 점프가 필요한지
# 만약, 가장 오른쪽 끝으로 갈 수 없는 경우에는 -1을 출력

import sys
input = sys.stdin.readline

ZERO = 0
INIT = 1001


n = int(input())
A = [ZERO] 
A += list(map(int,input().split(' ')))
D = [INIT for _ in range(n+1)] # i번째칸(i: 1~n)까지 최소 몇번의 점프가 필요한지
D[0] = ZERO
D[1] = ZERO
for i in range(1,n+1):
    # i+1에서 i+A[i]만큼 이동 가능
    range_ai = A[i]
    # print(f'{i}s range : {i} ~ {i+A[i]}, D[{i}]= {D[i]}')
    for j in range(i+1, i+range_ai+1):
        try:
            D[j] = min(D[i]+1,D[j])
            # print(f'D[{j}] = {D[j]}')
        except:
            continue
if D[n] == INIT:
    print(-1)
else:
    print(D[n])