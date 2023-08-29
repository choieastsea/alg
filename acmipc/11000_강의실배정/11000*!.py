from sys import stdin
from heapq import heappop, heappush

input = stdin.readline
if __name__ == "__main__":
    n = int(input())
    time_list = [list(map(int, input().split())) for _ in range(n)]
    time_list.sort(key=lambda x: x[0]) # 시작하는 순서대로 정렬
    class_heap = [time_list[0][1]] # 끝나는 시간을 담음.. 겹치면 새로운 것 추가
    for i in range(1,len(time_list)):
        strt, finish = time_list[i]
        # print(class_heap, strt, finish)
        current_finish = class_heap[0]
        if current_finish <= strt:
            # ok -> 기존 강의실 정보 갱신
            heappop(class_heap)
            heappush(class_heap, finish)
        else:
            # 겹치는 경우, 새로운 강의실 정보 추가함
            heappush(class_heap, finish)
    print(len(class_heap))
