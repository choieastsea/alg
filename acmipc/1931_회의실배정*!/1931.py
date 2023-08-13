from sys import stdin
input = stdin.readline

if __name__ == "__main__":
    n = int(input())
    meeting_list = []
    for i in range(n):
        meeting_list.append(list(map(int, input().split())))
    meeting_list = sorted(meeting_list, key= lambda x: (x[1], x[0]))  # 일찍 끝나고, 끝나는 시간 같다면 먼저 시작하는 순서대로 정렬
    # print(meeting_list)
    cnt = 0
    before_meeting_end_time = 0
    # 앞에서부터 채운다
    for meeting in meeting_list:
        strt, end = meeting
        # 이전 회의 끝나는 시간부터 시작 가능
        # print(strt, end, before_meeting_end_time)
        if before_meeting_end_time <= strt:
            cnt += 1
            before_meeting_end_time = end
    print(cnt)

"""
5
1 5
2 3
3 3
3 6
5 5
-> 3

2
3 3
1 5
-> 1
"""