from sys import stdin
input = stdin.readline

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))

answer_list = []
visited = [False for _ in range(n)]


def bt(cur_list):
    # print(f'bt called ({cur_list})')
    if len(cur_list) == m:
        answer_list.append(cur_list)
        return
    prev = -1
    for i in range(n):
        # print(f'arr[i] : {arr[i]}, prev : {prev}')
        if not visited[i] and prev != arr[i]:
            visited[i] = True
            bt(cur_list+[arr[i]])
            visited[i] = False
            prev = arr[i]

bt([])
for answer in answer_list:
    print(*answer)
