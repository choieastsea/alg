import sys
from collections import deque
input = sys.stdin.readline

def get_order_of_index(priorities, query):
    """
    priorities deque에서 index가 query인 문서의 출력 순서(1..)
    """
    order = 1
    # for _ in range(1):
    while True:
        # print(order, priorities)
        n = len(priorities)
        for _ in range(n):
            deque_size = len(priorities)
            # print(priorities)
            document1 = priorities[0]
            willPrint = True # 현재 맨 앞의 문서를 출력할지 여부
            for j in range(1,deque_size):
                document2 = priorities[j]
                if document1['priority'] < document2['priority']:
                    # document1 보다 큰게 존재 -> document 뒤로 빼야함
                    willPrint = False
                    priorities.append(priorities.popleft())
                    break
            if willPrint: # 맨 앞 보다 큰 우선순위를 갖는 문서 없는 경우
                if priorities.popleft()['index'] == query:
                    return order
                else:
                    order += 1
            

if __name__ == "__main__":
    case = int(input())
    answer = []
    for _ in range(case):
        n, query = map(int, input().split())
        priorities = deque([{"priority" : 0, "index" : i} for i in range(n)])
        p_list = list(map(int, input().split()))
        for i,p in enumerate(p_list):
            priorities[i]["priority"] = p
        print(get_order_of_index(priorities, query))
    # print(answer)


# input 
# 3
# 1 0
# 5
# 4 2
# 1 2 3 4
# 6 0
# 1 1 9 1 1 1

# output 
# 1
# 2
# 5