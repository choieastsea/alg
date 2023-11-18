T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
 
def find_cycle(word):
    """
    단어에서 반복되는 최소 단위 리턴
    cycle_str의 반복으로만 word 표현 가능해야함
    """
    for i in range(1, len(word)):
        cycle_str = word[:i]
        if cycle_str * (len(word)//i) == word:
            return cycle_str
    return word
 
 
def solution(str_1, str_2):
    """
    str_1, str_2 중에서 반복되는 substring이 같다면 return 'yes' else 'no'
    """
    if find_cycle(str_1) and find_cycle(str_1) == find_cycle(str_2):
        return 'yes'
    return 'no'
 
 
for test_case in range(1, T + 1):
    str_1, str_2 = input().split()
    print(f"#{test_case} {solution(str_1, str_2)}")