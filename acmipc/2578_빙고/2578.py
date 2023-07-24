import sys

def check_end(arr):
    #1차원 배열(1*25)에서 빙고가 성공하는지 판단
    bingo_count = 0
    # 1. 가로 줄 완성
    for i in range(5):
        if arr[5*i+0] == 0 and arr[5*i+1] == 0 and arr[5*i+2] == 0 and arr[5*i+3] == 0 and arr[5*i+4] == 0:
            bingo_count +=1
    # 2. 세로 줄 완성
        if arr[i] == 0 and arr[i+5] == 0 and arr[i+10] == 0 and arr[i+15] == 0 and arr[i+20] == 0:
            bingo_count +=1
    # 3. 대각선 완성(1)
    if arr[0] == 0 and arr[6] == 0 and arr[12] == 0 and arr[18] == 0 and arr[24] ==0:
        bingo_count +=1
    # 3. 대각선 완성(2)
    if arr[4] == 0 and arr[8] == 0 and arr[12] == 0 and arr[16] == 0 and arr[20] ==0:
        bingo_count +=1
    return bingo_count

# 1차원 배열로 입력받는게 좋을듯..?
input = []
for _ in range(10):
    input += list(map(int, sys.stdin.readline().split()))
answer = input[25:]
input = input[:25]

for round in range(0,25):
    ind = input.index(answer[round]) # 항상 양수일 것이다.
    input[ind] = 0
    if check_end(input) >=3:
        print(round+1)
        break

    
# 문제 : 다음 for loop에서도 해당 경우가 걸린다..! 따라서 한번에 3개의 빙고를 모두 체크할 필요가 있다.