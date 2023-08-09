from sys import stdin
input = stdin.readline

def getArea(strt, end, height):
    """
    strt 부터 end -1까지 height를 갖는 직사각형의 넓이
    """
    return (end-strt) * height

if __name__ =="__main__":
    planCnt = [0 for _ in range(367)] # 앞 뒤 비워둠
    n = int(input()) # number of plans
    for _ in range(n):
        strt, end = map(int, input().split())
        for day in range(strt, end+1):
            planCnt[day] += 1
    rect_strt_ind = 0
    rect_end_ind = 0
    height = 0
    area = 0
    for i, cnt in enumerate(planCnt):
        # print(i, cnt)
        if cnt == 0:
            rect_end_ind = i
            area += getArea(rect_strt_ind, rect_end_ind, height)
            # print(getArea(rect_strt_ind, rect_end_ind, height), 'added')
            rect_strt_ind = i
            height = 0
        elif rect_strt_ind == rect_end_ind:
            # print('area strt')
            rect_strt_ind = i
            height = cnt
        else:
            # print('area going...')
            height = max(height, cnt)
    print(area)
