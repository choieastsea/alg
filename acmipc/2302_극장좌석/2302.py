from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())  # 총 좌석 수(~40)
    m = int(input()) # 고정석 수(~n)
    fixedSeats = list(int(input()) for _ in range(m))
    # 자리당 경우의 수 (번호와 2이상 차이나지 않는 경우의 수)
    # [1] -> [1] : DP[1]
    # [1,2] -> [1,2] / [2,1] : DP[2] -> 2가지
    # [1,2,3] -> [1,2,3], [2,1,3] / [1,3,2] -> 3가지
    # [1,2,3,4] -> [1,2,3,4], [2,1,3,4], [1,3,2,4] /, [2,1,4,3], [1,2,4,3] : 새로 추가되는 거가 n-1번째 들어가면 추가되는 경우의 수 : DP[n-2] 가지
    # DP[n] : n개 이하의 좌석을 규칙 지켜가며 바뀌는 경우의 수
    # fixedSeats 있는것마다 배열 나누기
    sizeList = []
    prevFixedSeat = 0
    for seat in fixedSeats:
        sizeList.append(seat-prevFixedSeat-1)
        prevFixedSeat = seat
    sizeList.append(n-prevFixedSeat)
    # print('sizeList:',sizeList)
    dpSize = max(sizeList) + 1
    DP = [0,1,2]
    for i in range(3, dpSize):
        DP.append(DP[i-1] + DP[i-2])
    # print('dp:',DP)
    case = 1
    for size in sizeList:
        if DP[size] != 0:
            case *= DP[size]
    print(case)