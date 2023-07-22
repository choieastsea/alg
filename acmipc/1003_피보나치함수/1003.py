import sys
input = sys.stdin.readline

def fibo_count(n):
    """
    input : n
    output : fibonacci 함수에서 0과 1이 호출되는 횟수를 리턴
    """
    global fib_list
    current_list_len = len(fib_list)
    # print(f"current_len : {current_list_len}, n : {n}")
    if current_list_len >= n+1:
        # hit
        return fib_list[n]
    else:
        # miss
        for i in range(current_list_len, n+1):
            fib_list.append((fib_list[i-1][0]+fib_list[i-2][0], fib_list[i-1][1]+fib_list[i-2][1]))
        return fib_list[n]

if __name__ == "__main__":
    case = int(input())
    fib_list = [(1,0), (0,1)] # 0과 1의 호출 횟수를 튜플로 담아 리스트로 저장 & init basic case
    for _ in range(case):
        print(*fibo_count(int(input())))
