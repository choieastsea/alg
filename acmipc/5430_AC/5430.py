from sys import stdin
input = stdin.readline


def op(funcs:str, l):
    """
    l list에 대하여 funcs를 순차적으로 수행한다
    이후, strt~end까지 출력
    """
    if len(l) == 0:
        if funcs.find('D') >= 0:
            print('error')
            return
        else:
            print('[]')
            return
    strt = 0
    end = len(l)-1
    isForward = True
    for func in funcs:
        if func == 'R':
            # reverse
            strt, end = end, strt
            isForward = not isForward
        elif func == 'D':
            # popleft
            if isForward:
                strt += 1
            else:
                strt -= 1
    # print(strt, end, isForward)
    if isForward:
        if strt <= end+1:
            nl = l[strt:end+1]
            print(f'[{",".join(map(str,nl))}]')
        else:
            print('error')
    else:
        if strt >= end-1:
            nl = [l[i] for i in range(strt, end-1, -1)]
            print(f'[{",".join(map(str,nl))}]')
        else:
            print('error')


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        func_str = input().strip()
        size = int(input())
        # [1,2,3,4]로 입력 -> 정수형 배열로 변환
        if size > 0:
            inp = input().strip()[1:-1]
            l = list(map(int, inp.split(',')))
        else:
            inp = input()
            l = []
        op(func_str, l)
