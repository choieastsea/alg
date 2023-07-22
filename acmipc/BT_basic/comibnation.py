# 순열
def permutation(nums, visited, perm):
    if len(perm) == 2:  # 2개의 숫자를 선택한 경우
        print(perm)  # 선택된 숫자 출력
        return

    for i in range(len(nums)):
        if not visited[i]:
            visited[i] = True  # 해당 숫자 방문 처리
            perm.append(nums[i])  # 선택한 숫자 추가
            permutation(nums, visited, perm)  # 재귀 호출
            visited[i] = False  # 해당 숫자 방문 해제
            perm.pop()  # 마지막으로 선택한 숫자 제거

# 조합
def combination(nums, start, selected):
    if len(selected) == 2:  # 2개의 숫자를 선택한 경우
        print(selected)  # 선택된 숫자 출력
        return

    for i in range(start, len(nums)):
        selected.append(nums[i])  # 숫자 선택
        combination(nums, i + 1, selected)  # 재귀 호출
        selected.pop()  # 마지막으로 선택한 숫자 제거

# 테스트
nums = [1, 2, 3, 4, 5]
visited = [False] * len(nums)  # 방문 여부를 나타내는 리스트

print("순열:")
permutation(nums, visited, [])

print("조합:")
combination(nums, 0, [])
