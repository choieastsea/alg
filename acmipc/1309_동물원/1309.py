import sys
input = sys.stdin.readline

n = int(input())

# 2*n 배열에 사자를 배치하는 경우의 수(이웃하지 않아야 함)
# d = [0 for _ in range(n+1)] # d[i] : n*2 배열에서 사자를 이웃하지 않게 배치하는 경우의 수
# d[0] = 0
# d[1] = 3 # 왼쪽 오른쪽
# d[2] = 7
# for i in range(3,n+1):
#     d[i] = 2*d[i-1] + d[i-2]
# print(d[n]%9901)
d = [0, 0, 0] 
d[0] = 0
d[1] = 3 # 왼쪽 오른쪽
d[2] = 7
for i in range(3,n+1):
    d[i%3] = 2*d[(i-1)%3] + d[(i-2)%3]
print(d[n%3]%9901)
