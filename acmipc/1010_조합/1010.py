import sys
input = sys.stdin.readline

def mCn(m,n):
    return int(fact(m)/(fact(n)*fact(m-n)))

def fact(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

case = int(input())
for _ in range(case):
    n, m = map(int, input().split(' '))
    print(mCn(m,n))
