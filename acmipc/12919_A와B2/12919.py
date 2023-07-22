import sys
input = sys.stdin.readline
print = sys.stdout.write

def func1(s:str):
    return s + 'A'

def func2(s:str):
    return (s+'B')[::-1]

def func3(t:str):
    if t[-1] == 'A':
        return t[:-1]
    return ''

def func4(t:str):
    if t[0] == 'B':
        return t[::-1][:-1]
    return ''

def sToT(S, T):
    # print(f'S : {S}, T: {T}\n')
    if len(T) == 0:
        return
    if len(S) >= len(T):
        if S == T:
            print("1\n")
            exit(0)
    else:
        # sToT(S,T)
        # sToT(func1(S),T)
        # sToT(func2(S),T)
        sToT(S,func3(T))
        sToT(S,func4(T))


S = input()[:-1]
T = input()[:-1]

sToT(S,T)
print("0\n")

# T에서부터 S로 가는 것이 조건 단계에서 search space를 확장하지 않게 하므로, 더 빠르게 가능하다는 것을 알 수 있어야 한다!!!
