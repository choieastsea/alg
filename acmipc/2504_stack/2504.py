import sys
input = sys.stdin.readline

CURLY_OPEN = '('
CURLY_CLOSE = ')'
BRACKET_OPEN = '['
BRACKET_CLOSE = ']'

line = input()
# line = '((()'
stack = []

for char in line:
    # print('char : ',char)
    if char == CURLY_OPEN: #(
        stack.append(char)
    elif char == CURLY_CLOSE:#)
        acc = 0
        while True:
            if len(stack) > 0:
                c = stack.pop()
                # print('c =',c)
                if c is CURLY_OPEN:
                    # open 찾은 경우,
                    if acc ==0:
                        acc += 2
                    else:
                        acc *= 2
                    break
                else:
                    # open 찾을 때까지 숫자 pop
                    if type(c) == int:  # 숫자인 경우
                        acc += int(c)
                    else:
                        print(0) # 에러 케이스
                        exit(0)
            else:
                print(0)
                exit(0)
        stack.append(acc)
    elif char == BRACKET_OPEN: # [
        stack.append(char)
    elif char == BRACKET_CLOSE:# ]
        acc = 0
        while True:
            if len(stack) > 0:
                c = stack.pop()
                # print('c =',c)
                if c is BRACKET_OPEN:
                    # open 찾은 경우,
                    if acc ==0:
                        acc += 3
                    else:
                        acc *= 3
                    break
                else:
                    # open 찾을 때까지 숫자 pop
                    if type(c) == int:  # 숫자인 경우
                        acc += int(c)
                    else:
                        print(0) # 에러 케이스
                        exit(0)
            else:
                print(0)
                exit(0)
        stack.append(acc)
    else:
        # 숫자 적혀 있는 경우
        # 안에 있는 것들 다 더해서 곱해줘야함
        pass

    # print(char,":",stack)
result = 0
for el in stack:
    if type(el) == int:
        result += el
    else:
        print(0)
        exit(0)
print(result)

"""
input : (()[[]])([])
stack trend
( : ['(']
( : ['(', '(']
) : ['(', 2]
[ : ['(', 2, '[']
[ : ['(', 2, '[', '[']
] : ['(', 2, '[', 3]
] : ['(', 2, 9]
) : [22]
( : [22, '(']
[ : [22, '(', '[']
] : [22, '(', 3]
) : [22, 6]
"""