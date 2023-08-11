from sys import stdin
input = stdin.readline

class Frame():
    def __init__(self, num) -> None:
        self.num = num # 학생 번호
        self.isIn = False
        self.recommendationCnt = 0
        self.duration = 0
    def __str__(self) -> str:
        return f'num : {self.num}, ({self.isIn},{self.recommendationCnt},{self.duration})'

if __name__ == "__main__":
    n = int(input())
    k = int(input())
    recommends = list(map(int,input().split()))
    students = [Frame(i) for i in range(100)] # i번 학생에 대한 정보
    fullCnt = 0 # 얼마나 차있는지
    for i, recommend in enumerate(recommends):
        # print(f'--------------day{i}--------------------, cnt:{fullCnt}, input:{recommend-1}')
        # for student in students:
        #     if student.isIn:
        #         print(student.num, end=' ')
        # print()
        # 처음에 frame에 있는 애들 duration 증가
        for student in students:
            if student.isIn:
                # 안에 있는 애들은 개시 기간 증가
                student.duration += 1
        # 추천 로직
        person = recommend - 1
        if students[person].isIn:
            # print('case1')
            # 있다면 추천수 올려줌
            students[person].recommendationCnt += 1
        else:
            # 없다면 넣어줄건데
            # 1. 꽉차지 않은 경우 -> 넣어주기
            # 2. 꽉찬 경우 -> 소팅해서 비워주기
            if fullCnt < n:
                # print('case2')
                # frame에 추가
                fullCnt += 1
                students[person].isIn = True
                students[person].recommendationCnt = 1
            elif fullCnt == n:
                # print('case3')
                # 꽉찬 경우, 추천수 > 개시기간 순으로 소팅해서 우선순위 낮은 1개를 버린다(is_in : false, reco_cnt : 0)
                currentStudents = [students[i] for i in range(100) if students[i].isIn] # 있는 놈들만 골라서 소팅
                sorted_students = sorted(currentStudents, key = lambda x: (x.recommendationCnt, -x.duration)) # 개시기간은 긴게 안좋은것
                # print(*sorted_students)
                # 넌 나가라 ~
                # print(sorted_students[0])
                sorted_students[0].isIn = False
                sorted_students[0].recommendationCnt = 0
                sorted_students[0].duration = 0
                # 넌 들어와라 ~
                students[person].isIn = True
                students[person].recommendationCnt = 1
                students[person].duration = 0

    for frame in students:
        if frame.isIn:
            print(frame.num+1, end=' ')
    print()