import sys 
input = sys.stdin.readline

n_stairs = int(input())
S = [0]
for _ in range(n_stairs):
    S.append(int(input()))
if n_stairs == 1:
    print(S[1])
    exit()
elif n_stairs ==2:
    print(S[1]+S[2])
    exit()

ZERO = 0
D = [ZERO for _ in range(n_stairs+1)]
D[0] = ZERO
D[1] = S[1]
D[2] = D[1]+S[2]
for i in range(3,n_stairs+1):
    # i-1 과 i-2의 값 비교하여 더 큰 값 선택
    if D[i-1] > D[i-2]:
        # D[i-1]이 연속으로 왔었는지 확인
        if D[i-1] == D[i-4] + S[i-2] + S[i-1]:
                # 연속으로 왔다면, D[i-2]과 D[i-3] + S[i-1]를 비교해야함
            if D[i-2] < D[i-3] + S[i-1]:
                # 오른쪽이 더 크다면, D[i]는 i-3,i-1,i를 선택해야함
                D[i] = D[i-3] + S[i-1] + S[i]
            else:
                # 왼쪽이 더 크다면, D[i]는 i-2, i를 선택해야함
                D[i] = D[i-2] + S[i]
        else:
                #연속으로 온 것이 아니면, -1 선택
                D[i] = D[i-1] + S[i]
    else:
        D[i] = D[i-2] + S[i]

print(D[n_stairs])