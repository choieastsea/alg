class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[1]) # 끝나는 범위 오름차순 정렬
        # 이전 max가 min보다 작다면 겹치는 것.!
        cur_min, cur_max  = points[0] # 현재 가능한 범위
        cnt = 1
        for strt, end in points:
            if strt <= cur_max:
                # 이전과 겹침!
                cur_min = max(strt, cur_min)
                cur_max = min(end, cur_max)
            else:
                cnt += 1
                cur_min = strt
                cur_max = end
        return cnt