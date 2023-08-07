from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    heights = list(map(int, input().split()))
    stack = [(-1,10**9)] # index, height
    for current_index in range(len(heights)):
        current_height = heights[current_index]
        while len(stack) > 1:
            # print(stack, (current_height,current_index))
            before_index, before_height = stack[-1]
            if before_height <= current_height:
                # 앞의 것들을 다 볼 필요는 없으므로! pop해가면서 가자.
                stack.pop()
                continue
            else:
                print(before_index + 1)
                stack.append((current_index, current_height))
                break
        if len(stack) == 1:
            stack.append((current_index, current_height))
            print(0)
        
