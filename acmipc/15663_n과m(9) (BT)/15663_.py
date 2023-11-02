from sys import stdin
from collections import Counter

input = stdin.readline
n,m = map(int, input().split())
arr = list(map(int,input().split()))
arr.sort() # 증가하는 순서대로 뽑아야하므로 sort
remain = Counter(arr)
# n 개의 자연수 arr 중에서 m개를 고르기!(단, 중복은 허용하지 않음)
answer_set = set()
answer_list = list()
def bt(cur_list:list):
    if len(cur_list) == m:
        # 종료 조건. 기존 조합이 있나 확인할 필요 있음
        cur_tuple = tuple(cur_list)
        if not cur_tuple in answer_set:
            answer_set.add(cur_tuple)
            answer_list.append(cur_tuple)
        return
    for el in arr:
        if remain[el] > 0:
            remain[el] -= 1
            bt(cur_list+[el])
            remain[el] += 1
bt([])

for answer in answer_list:
    print(*answer)