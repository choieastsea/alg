import sys
input = sys.stdin.readline

lines = int(input())
gom_set = set()
gom_count = 0

for _ in range(lines):
    line = input()[:-1]
    if line == 'ENTER':
        # count 추가
        gom_count += len(gom_set)
        # set 초기화
        gom_set.clear()
    else:
        gom_set.add(line)
        
if len(gom_set) != 0:
    gom_count += len(gom_set)
    gom_set.clear()

print(gom_count)
