def solution(n):
    answer = []
    def hanoi(n,strt,end,rest):
        """
        n개의 원판을 strt에서 end로 옮긴다
        """
        # print(f'{n}개를 {strt}에서 {end}로 옮기기')
        if n == 1:
            answer.append([strt,end])
            return
        hanoi(n-1,strt,rest,end)
        hanoi(1,strt,end,rest)
        hanoi(n-1,rest,end,strt)
    hanoi(n,1,3,2)
    return answer