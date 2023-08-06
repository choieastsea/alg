from sys import stdin
input = stdin.readline

def calc(a,b,c):
    """
    a**b를 c로 나눈 나머지를 리턴
    a**b%c = (a**(b/2)%c * a**(b/2)%c)%c 로 변환
    """
    if b == 1:
        # basic case
        return a % c
    else:
        # b 홀짝에 따라 다름
        if b%2 == 0:
            return calc(a,b//2,c) ** 2 % c
        else:
            # b : 11 -> a**11%c = ((a**5%c) * (a**5%c) * a) % c
            # return calc(a,b//2,c) * calc(a,b//2 + 1,c) % c
            return (calc(a,b//2, c) ** 2 * a) % c

if __name__ == "__main__":
    A,B,C = map(int, input().split())
    # A를 B번 곱한 수를 C로 나눈 나머지를 출력 (A,B,C <= 2,147,483,647)
    # print(A**B%C) -> time over!
    print(calc(A,B,C))
    