import sys

input = sys.stdin.readline

n = int(input())
array = []
histogram = [0 for _ in range(8001)] # histogram[i] : i-4000 이 몇번 나타났는지
max_count = 0 # mode index form histogram
for _ in range(n):
    number = int(input())
    array.append(number)
    # histogram for mode
    histogram[number+4000] += 1
    if histogram[number+4000] > max_count:
        max_count = histogram[number+4000]

sorted_array = sorted(array) # sort for median

# max_count와 동일한 count갖는 index 찾기
mode_candidate = []
for idx, cnt in enumerate(histogram):
    if cnt == max_count:
        mode_candidate.append(idx-4000)
    if len(mode_candidate) >= 2:
        break
# print()
print(round(sum(array)/n)) # mean
print(sorted_array[n//2]) # median
# print(mode_candidate)
print(mode_candidate[0] if len(mode_candidate) == 1 else mode_candidate[1]) # mode
print(sorted_array[n-1]-sorted_array[0]) # max - min
