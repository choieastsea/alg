from sys import stdin

input = stdin.readline

def updateDP(i):
    """
    i+1에서부터 i+6까지의 경로를 업데이트
    만약, 그 중에 뱀이나 사다리 있다면 그 주변도 재귀적으로 업데이트...
    """
    global game
    global DP
    print(f'update({i})')
    for k in range(1,7):
        if i + k <= 100:
            print(f'i + k: {i+k}, game[i+k] : {game[i+k]}')
            to = game[i+k] # 다음칸 (사다리나 뱀인 경우에도...)
            DP[to] = min(DP[to], DP[i] + 1)
            if to != i+k: # 사다리나 뱀인 경우, recursion
                print(f'should recursion to {to}')
                DP[i+k] = min(DP[i+k], DP[i] + 1)
                # game[i+k] = i+k # ...
                updateDP(to)
                print(f'recursion {to} is ended')
                print(DP)


if __name__ == "__main__":
    DP = [100 for _ in range(101)] # DP[i] : i번칸에 도착하기 위해 주사위 최소 몇번 굴려야 하는지
    game = [i for i in range(101)] # game[i] : i번칸에 도착하면, 실제 어디로 가게 되는지
    n, m = map(int, input().split())
    for _ in range(n):
        # 사다리 정보 -> 해당 인덱스에 값을 넣어줌
        strt, end = map(int, input().split())
        game[strt] = end
    for __ in range(int(m)):
        # 뱀 정보
        strt, end = map(int, input().split())
        game[strt] = end
    DP[0] = 0
    DP[1] = 0
    for i in range(1,101, 6):
        updateDP(i)
    print(DP)
    print(DP[100])
    # print(DP)

    #DP가 안되는 이유!
    # 재귀적으로 수행해야하는데, 이 경우 업데이트되는 값의 최소를 보장하지 못하므로 무한 재귀에 빠지게 될 것임