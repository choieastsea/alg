def getMinCount(lottos, win_nums):
    """
    현재 있는 것들 중에 일치하는 것, 일치하지 않는것, 알수 없는 것 리턴
    """
    correct = 0
    incorrect = 0
    unknown = 0
    for lotto in lottos:
        if lotto == 0:
            unknown += 1
        elif lotto in win_nums:
            correct += 1
        else:
            incorrect += 1
    return (correct, incorrect, unknown)
def getRank(correct):
    """
    6개 중 correct 만큼 맞았을 때, 순위를 리턴
    """
    if correct >=2:
        return 7-correct
    else:
        return 6

def solution(lottos, win_nums):
    """
    lottos : 0 또는 숫자
    win_nums : 6개 정답
    최고, 최저 순위를 리턴
    """
    correct, incorrect, unknown = getMinCount(lottos, win_nums)
    # unknown 에 따라 correct 증가 가능
    max_correct = correct + unknown
    answer = [getRank(max_correct), getRank(correct)]
    return answer

print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))   #[3,5]
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))    #[1, 6]
print(solution([45, 4, 35, 20, 3, 9],[20, 9, 3, 45, 4, 35]))    #[1, 1]