from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input()) # 2~100,000
    potions = list(map(int, input().split())) # 정렬된 채로 주어짐..! => BS? 2pointer?
    # 합이 0에 가장 가까운 조합을 출력 (동점이라면 아무거나) <=> abs(a+b)의 최솟값이 되는 a,b를 찾는다
    currentMin = ((-1,-1), 2*10**9+1) # 조합, 합의 절댓값
    left = 0
    right = n-1
    while left < right:
        # print(left, right)
        leftVal = potions[left]
        rightVal = potions[right]
        twoSum = leftVal + rightVal
        absSum = abs(twoSum)
        if absSum < currentMin[1]:
            # 합의 절댓값의 최솟값
            currentMin = ((left, right), absSum)
        if twoSum == 0:
            currentMin = ((left, right), twoSum)
            break
        elif twoSum < 0: # left가 더 절댓값 큼 -> 뒤로 당길 필요 있음
            left += 1
        else: # right가 더 절댓값 큼 -> 앞으로 당길 필요 있음
            right -= 1
    # print(currentMin)
    idx1, idx2 = currentMin[0]
    print(potions[idx1],potions[idx2])
