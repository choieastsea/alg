#import sys
#sys.stdin = open("input.txt", "r")
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
import math
 
 
def solution(a,b):
    """
    a에서 b 까지의 자연수들의 최대공약수를 리턴
    """
    if a == b:
        return a
    elif b - a == 1:
        return 1
    cur_gcd = a
    for i in range(a, b+1):
        cur_gcd = math.gcd(cur_gcd, i)
        if cur_gcd == 1:
            return 1
    return cur_gcd
 
 
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    print(f"#{test_case} {solution(a,b)}")