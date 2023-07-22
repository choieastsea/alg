import sys
input = sys.stdin.readline

if __name__ == "__main__":
    N,H = map(int, input().split())
    from_btm = [0 for _ in range(H)]  # 밑에서부터 나는 장애물 -> from_btm[i] = 높이 i 인것의 갯수
    from_top = [0 for _ in range(H)]  # 위에서부터 나는 장애물
    for _ in range(N//2):
        h1 = int(input())
        from_btm[h1] = from_btm[h1] + 1
        h2 = H - int(input())
        from_top[h2] = from_top[h2] + 1

    B = [N//2 for _ in range(H)] # from_btm 배열에서, i 이상인 것의 갯수
    T = [0 for _ in range(H)] # from_top 배열에서, H-i 이상인 것의 갯수
    # S = [N]
    min_sum = B[0] + T[0]
    min_cnt = 1
    for i in range(1,H):
        # print(i)
        B[i] = B[i-1] - from_btm[i]
        T[i] = T[i-1] + from_top[i]
        # S.append(B[i] + T[i])
        S = B[i] + T[i]
        if min_sum == S:
            min_cnt += 1
        elif min_sum > S:
            min_sum = S
            min_cnt = 1
    # print(B)
    # print(T)
    print(min_sum,min_cnt)
