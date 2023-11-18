#import sys
#sys.stdin = open("input.txt", "r")
from collections import Counter
T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.


def solution(dump_cnt, heights):
    """
    heights 배열에서 dump_cnt 만큼 옮겨 담아서 최대한 flatten 했을 때,
    최대와 최소의 차이
    """
    min_height, max_height = min(heights), max(heights)
    heights_counter = Counter(heights)
    cnt = 0
    print(heights_counter)
    while cnt < dump_cnt:
        if heights_counter[min_height] > 0 and heights_counter[max_height] > 0:
            heights_counter[max_height] -= 1
            heights_counter[max_height-1] += 1
            heights_counter[min_height] -= 1
            heights_counter[min_height + 1] += 1
            cnt += 1
        if heights_counter[min_height] == 0:
            del heights_counter[min_height]
            min_height += 1
        elif heights_counter[max_height] == 0:
            del heights_counter[max_height]
            max_height -= 1
    # print(heights_counter)
    return max_height - min_height


for test_case in range(1, T + 1):
    dump_cnt = int(input())
    heights = list(map(int, input().split()))
    print(f"#{test_case} {solution(dump_cnt, heights)}")