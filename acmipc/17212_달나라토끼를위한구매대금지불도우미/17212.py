# 동전 : 1원, 2원, 5원, 7원 
# 동전의 갯수가 최소가 되도록 지불해야함
# 최소가 되도록 하는 동전의 수
import sys
input = sys.stdin.readline

money = int(input())

if money < 7:
    size = 7
else:
    size = money
D = [i//7 if i%7 == 0 else i//5 if i%5 == 0 else i//2 if i%2 == 0 else i for i in range(size+1)]

for i in range(1,money+1):
    D[i] = min(min(D[i-2], D[i-5], D[i-7]) + 1, D[i])
print(D[money])    