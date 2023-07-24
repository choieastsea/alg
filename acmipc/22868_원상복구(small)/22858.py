import copy
def print_list(list):
    for el in list:
        print(el,end=' ')
    print()
(card_count, shuffle_count) = tuple(map(int, input().split()))
s = list(map(int, input().split()))
d = list(map(int, input().split()))
# print(card_count, shuffle_count)
p = [0 for _ in range(card_count)]
# shuffle_count = shuffle_count%card_count    # 카드 n개이면, n회 셔플마다 제자리로 돌아오지 않나 싶은데...
for _ in range(shuffle_count):
    for i in range(card_count):
        p[d[i]-1] = s[i]
    # print(f'after {_} : {p}')
    s = copy.deepcopy(p)
# print(p[1:])
print_list(p)
