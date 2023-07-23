import sys
input = sys.stdin.readline

def makeNextNumber(n):
    """
    3자리 이상의 수가 들어올 때, 이를 a/b/c로 나눠서 a+b+c를 리턴
    """
    n_str = str(n)
    nextNumbers = []
    digit_length = len(n_str) # XX -> 2자리,  XXX -> 3자리
    for i in range(digit_length - 2):
        for j in range(i + 1 , digit_length - 1):
            # print(n_str[:i+1],n_str[i+1:j+1],n_str[j+1:])
            nextNumbers.append(int(n_str[:i+1]) + int(n_str[i+1:j+1]) + int(n_str[j+1:]))
    return nextNumbers

def countHolsu(n):
    """
    숫자 n에서 홀수가 몇개가 있는지 리턴
    """
    n_str = str(n)
    cnt = 0
    for chr in n_str:
        if int(chr)%2 != 0:
            cnt += 1
    return cnt

def calc(n, cnt):
    """
    n에 특수한 연산을 수행했을 때, 과정마다 나오는 홀수 갯수의 합(cnt)을 계산
    해당 결과를 기존과 비교하여 min, max_result 값 업데이트
    """
    global min_result, max_result
    cnt += countHolsu(n)
    # print(f'n : {n}, cnt : {cnt}')
    if n < 10:
        # BASIC case
        if min_result > cnt:
            min_result = cnt
        if max_result < cnt:
            max_result = cnt
    else:
        # RECURSION case
        if n >= 100:
            # 세자리 이상 -> 3개의 파트로 나눠서 calc 계산
            nextNumbers = makeNextNumber(n)
            for i in nextNumbers:
                calc(i, cnt)
        elif n >= 10:
            calc(n//10 + n%10, cnt)

if __name__ == "__main__":
    n = int(input())
    min_result = 26 # => 9 + 7 + 5 + 3 + 1
    max_result = 0
    calc(n, 0)
    print(min_result, max_result)