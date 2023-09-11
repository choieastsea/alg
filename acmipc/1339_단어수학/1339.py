from sys import stdin
from collections import Counter
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    str_list = list(input().rstrip() for _ in range(n))
    sum_counter = {}
    for str in str_list:
        size = len(str)
        for i in range(size):
            char = str[i]
            if char in sum_counter:
                sum_counter[char] += 10**(size-1-i)
            else:
                sum_counter[char] = 10**(size-1-i)
    # 높은 순서부터 9부터 배정
    num = 9
    total = 0
    for key, value in Counter(sum_counter).most_common(len(sum_counter)):
        total += value * num
        num -= 1
    print(total)
