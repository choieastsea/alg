from sys import stdin
from itertools import combinations
input = stdin.readline

if __name__ =="__main__":
    n = int(input()) # n ~ 1,000,000
    # 0~9에서 k(1~10)개를 뽑아서 숫자를 만들자. 그 중 줄어드는 숫자를 배열에 추가해준다
    result = []
    for k in range(1,11):
        for combination in combinations(range(0,10), k): # 0~9에서 k개 뽑는 조합
            comb_list = sorted(combination, reverse=True)
            result.append(int(''.join(map(str,comb_list)))) # 줄어드는 수
    result.sort()
    if n <= len(result):
        # print("".join(result[n-1]))
        print(result[n-1])
    else:
        print(-1)