#0에서부터 9까지의 숫자로 이루어진 N개의 숫자가 나열된 수열이 있다.
#그 수열 안에서 연속해서 커지거나(같은 것 포함), 
#혹은 연속해서 작아지는(같은 것 포함) 수열 중 가장 길이가 긴 것을 찾아내어 그 길이를 출력하는 프로그램을 작성하라.

import sys
INIT = 1
ZERO = 0
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split(' ')))

# 정방향과 역방향으로 고려하면 될듯..?
INC_D = [INIT for _ in range(n)] # INC_D[i]는 '0~i까지 연속해서 커지는 수열 중 최대 길이'를 저장
DEC_D = [INIT for _ in range(n)] # DEC_D[i]는 '~~최소 길이'를 저장
# max_value = arr[0] # 증가하고 있는 경우 그 증가분 중 최댓값
inc_length = 1 # 현재 증가하고 있는 경우 연속된 수열의 길이
dec_length = 1 # 현재 감소하고 있는 경우 연속된 수열의 길이
for i in range(1, n):
    if arr[i-1] <= arr[i]:
        #증가한 경우. 계속 증가하는건지 / 이제 증가하기 시작하는건지
        inc_length += 1
        INC_D[i] = max(INC_D[i-1], inc_length)
    else:
        #감소한 경우
        inc_length = 1
        INC_D[i] = max(INC_D[i-1], inc_length)
        # print(f'{i}) case3, INC_D[{i}] = {INC_D[i]}')
    
    #감소 배열
    if arr[i-1] >= arr[i]:
        #감소한 경우. 계속 감소하는건지 / 이제 감소하기 시작하는건지
        dec_length += 1
        DEC_D[i] = max(DEC_D[i-1], dec_length)
    else:
        #증가한 경우
        dec_length = 1
        DEC_D[i] = max(DEC_D[i-1], dec_length)
        
print(max(DEC_D[n-1],INC_D[n-1]))

# print(*INC_D)
# print(*DEC_D)