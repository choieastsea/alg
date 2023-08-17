from sys import stdin
input = stdin.readline

def BT(i,n):
    """
    현재 n(string)일때, i자릿수 만들기
    """
    global i_list
    if len(n) == i:
        # basic case
        i_list.append(int(n))
    else:
        # make next num
        last_num = int(n[-1])
        for next_num in range(last_num-1, -1, -1):
            BT(i,n+str(next_num))
        
def makeDecNum(i,k,cnt):
    """
    i자릿수, k로 시작하는 cnt번째 감소 숫자 리턴
    BT로 k로 시작하는 i자릿수 만든 후에 sorting하고 cnt번째 출력하면 될듯
    """
    global i_list
    BT(i,str(k))
    # print(sorted(i_list))
    return sorted(i_list)[cnt]
    

if __name__ =="__main__":
    n = int(input()) # n ~ 1,000,000
    # n번째로 작은 줄어드는 수를 출력, 없을 때는 -1을 출력
    """
    # 한자리
    0,1,2,3,4,5,6,7,8,9,10
    10 (9+1)
    x => 10

    # 두자리
    1x => 1
    2x => 2
    3x => 3
    ...
    9x => 9
    # 세자리
    2xx => 21x => [1]
    3xx => 32x + 31x => 2 + 1 => [3]
    4xx => 43x + 42x + 41x => 3 + 2 + 1=> [6]
    5xx => 54x + 53x + 52x + 51x=> 4 + 3 + 2 +1=> [10]
    6xx => 65x + 64x + 63x + 62x +61x => 5+4+3+2+1 => [15]
    ...
    9xx => 98x + 97x + 96x + ... + 91x => 8+7+...+1 => [36]
    # 네자리
    3xxx => 32xx => [1]
    4xxx => 43xx + 42xx => 3 + 1 => [4]
    5xxx => 54xx + 53xx + 52xx => 6 + 3 + 1 [10]
    ...
    # 10자리
    9xxxxxxxxx => 98xxxxxxxx => 987xxxxxxx => ... => 9876543210 => [1]
    """
    if n <= 10:
        # 1자리수 일때 1번째 작은거 0
        print(n-1)
    else:
        i_list = []
        cnt_matrix = [[0 for _ in range(10)] for _ in range(11)] # cnt_matrix[i][k] : i자리이고, k로 시작하는 줄어드는 수의 숫자
        cnt_matrix[1] = [1 for _ in range(10)] # 1자리일때는 1로 초기화
        acc_cnt = 10
        for i in range(2, 11):
            acc = 0
            for k in range(len(cnt_matrix[i])):
                if k >= 1:
                    acc += cnt_matrix[i-1][k-1]
                    cnt_matrix[i][k] = acc
                    acc_cnt += acc
                    if acc_cnt >= n:
                        # print(f'{i}자리 {k}로 시작하는 것부터 보면 될듯, {n- acc_cnt + acc}개 더 가봐')
                        print(makeDecNum(i,k,n-acc_cnt+acc-1))
                        exit(0)
        print(-1)
        # print(cnt_matrix)

        # 1023이 마지막인감?