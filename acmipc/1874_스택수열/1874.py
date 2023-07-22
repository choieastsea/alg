import sys
input = sys.stdin.readline

if __name__ == '__main__':
    result_list = []
    n = int(input())
    stack = [1]
    # print("+1")
    result_list.append('+')
    last_el = 1
    for i in range(n):
        query = int(input())
        while last_el < query:
            stack.append(last_el + 1)
            # print(f"+{last_el+1}")
            result_list.append('+')
            last_el += 1
        # print(f'after push, {stack}')
        while True:
            if len(stack) == 0:
                print('NO')
                exit(0)
            popped = stack.pop()
            result_list.append('-')
            if popped == query:
                break
    for result in result_list:
        print(result)
        # print(f'after pop, {stack}')
        