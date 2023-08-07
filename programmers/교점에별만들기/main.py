INF = 10**10
def getPoints(lines):
    points = []
    minx, miny, maxx, maxy = INF,INF,-INF,-INF
    for i in range(len(lines)): # 1000,000
        for j in range(i+1, len(lines)):
            a,b,e = lines[i]
            c,d,f = lines[j]
            if a*d != b*c:
                # 평행 / 일치 안됨
                x = (b*f-e*d)/(a*d-b*c)
                y = (e*c-a*f)/(a*d-b*c)
                if x - int(x) == 0 and y - int(y) == 0:
                    # 정수 좌표만 표현
                    x = int(x)
                    y = int(y)
                    minx = min(x,minx)
                    maxx = max(x,maxx)
                    miny = min(y,miny)
                    maxy = max(y,maxy)
                    points.append((x,y))
    return points, ((minx,miny),(maxx,maxy))

def solution(lines):
    points, ((minx,miny),(maxx,maxy)) = getPoints(lines)
    rect = [['.' for _ in range(maxx-minx+1)] for _ in range(maxy-miny+1)]
    for x,y in points:
        rect[maxy-y][x-minx] = '*'
    return [''.join(i) for i in rect]

print(solution([[2, -1, 4], [-2, -1, 4], [0, -1, 1], [5, -8, -12], [5, 8, 12]]))
# solution([[0, 1, -1], [1, 0, -1], [1, 0, 1]])
# solution([[1, -1, 0], [2, -1, 0]])
# print(solution([[2,1,0],[1,-1,0],[1,1,-2]]))
