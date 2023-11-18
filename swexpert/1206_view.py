T = 10
 
 
def solution(buildings):
    """
    building 리스트가 주어졌을 때,
    (좌우로 2개씩 여유 있는 경우를 조망권 있다고 함) -> 본인 기준 왼쪽 2개, 오른쪽 2개의 최댓값을 갖고 다니자
    조망권있는 집의 수를 리턴
    """
    acc = 0
    for i in range(len(buildings)):
        neighbor_max = max(buildings[i-2:i] + buildings[i+1:i+3])
        acc += (buildings[i]-neighbor_max) if buildings[i] > neighbor_max else 0
    return acc
 
 
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _ = input()
    buildings_input = list(map(int, input().split()))
    print(f"#{test_case} {solution(buildings_input)}")