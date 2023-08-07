from sys import stdin
input = stdin.readline

if __name__ =="__main__":
    n = int(input())
    heights = list(map(int, input().split()))
    # 자신보다 앞에 있으면서 딱 자기보다 큰 녀석
    wall = (0,[]) # 왼쪽 벽 index, 벽높이보다 작은 녀석들(index)
    answer = []
    for i, height in enumerate(heights):
        # print(f'{i} ) wall : {wall}, height : {height}')
        if height < heights[wall[0]]:
            # 현재 벽보다 작다면 벽에 막히는 것임
            # print('case1')
            wall[1].append(i)
            # print('wall:',wall)
            flag = -1
            for prior in wall[1]:
                if heights[prior] > height:
                    flag = prior
            if flag == -1:
                # height가 wall보단 작지만 나머지보단 큼
                # print(wall[0] + 1)
                answer.append(wall[0]+1)
            else:
                # print(flag + 1)
                answer.append(flag+1)
            # print(wall[0]+1)
        else:
            # 현재 벽보다 자기가 크다면,,, index 업데이트
            # print('case2')
            wall = (i, [])
            # print('wall:',wall)
            # print(0)
            answer.append(0)
    print(*answer)
