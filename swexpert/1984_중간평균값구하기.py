T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
 
 
def solution(num_list):
    """
    nums 배열에서 최대와 최소를 제외한 평균을 리턴
    """
    max_num = max(num_list)
    min_num = min(num_list)
    acc = 0
    cnt = 0
    for num in num_list:
        if num not in (max_num, min_num):
            acc += num
            cnt += 1
    return round(acc / cnt)
 
 
for test_case in range(1, T + 1):
    nums = list(map(int, input().split()))
    print(f"#{test_case} {solution(nums)}")