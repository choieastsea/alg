from sys import stdin
input = stdin.readline

if __name__ ==  "__main__":
    n = int(input())
    stack = []
    for _ in range(n):
        op, ch, num = input().split()
        if op == "type":
            time = int(num)
            stack.append((0,ch,time))
        else:
            duration = int(ch)
            time = int(num)
            stack.append((1,duration,time))
    output = ''
    limit_time = 10**10
    while stack:
        op, do, time = stack.pop() # do는 문자거나 숫자
        if time >= limit_time:
            continue
        if op == 0:
            # 문자열 넣기
            output += do
        else:
            # update limit time
            limit_time = time-do
    print(output[::-1])