from sys import stdin
input = stdin.readline

def get8(str_num:str):
    """
    해당 숫자에 8이 어디에 들어있는지 88999 -> [T,T,F,F,F]
    """
    info = [False for _ in range(len(str_num))]
    for i in range(len(str_num)):
        if str_num[i] == '8':
            info[i] = True
    return info

def solution(l:str,r:str):
    """
    L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수
    L,R ~ 2,000,000,000
    """
    min_cnt = 0

    while True:
        # print(l,r)
        lcount = get8(l)
        rcount = get8(r)
        if len(lcount) < len(rcount):
            # 자릿수 차이나는 경우 -> 무줴~건 0
            return min_cnt
        else:
            # 자릿수 같은 경우
            if len(lcount) == 1:
                return min_cnt + 1 if (l=='8' and r == '8') else min_cnt
            
            if lcount[0] and rcount[0]:
                min_cnt += 1

            if l[0] != r[0]:
                r = 'xx'+r[2:]

            l = l[1:]
            r = r[1:]
    

if __name__ == "__main__":
    l,r = input().split()
    print(solution(l,r))
    
    """
    근데, 이문제는 greedy하게 풀면 되는 듯 하다.
    l과 r의 자릿수가 같다면,
    각 자리를 비교하면서 둘다 8이면 cnt += 1, 다르면 cnt=0 바로 리턴, 둘다 같으면 continue 하면 됨..!
    """