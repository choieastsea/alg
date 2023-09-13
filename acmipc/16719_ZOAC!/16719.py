from sys import stdin
input = stdin.readline


def makeWord(l, r):
    """
    l~r에서 가장 작은 것을 찾아 단어를 기존 단어에 붙혀서 출력하고, 그 다음 부분(min기준 오른쪽 -> 왼쪽)을 호출하여 단어 만든다
    """
    if l < 0 or l > n-1 or r < 0 or r > n-1 or l > r:
        # 범위 벗어남
        pass
    else:
        min_idx = findMin(l,r)
        word[min_idx] = ch_list[min_idx]
        print(''.join(word))
        makeWord(min_idx+1,r)
        makeWord(l,min_idx-1)
        

def findMin(l, r):
    # [l,r]에서 가장 작은것을 찾는다
    min_idx = l
    for i in range(l, r + 1):
        if ch_list[min_idx] > ch_list[i]:
            min_idx = i
    return min_idx


if __name__ == "__main__":
    ch_list = list(input().strip())  # 최대 100글자
    n = len(ch_list)
    word = ['' for _ in range(len(ch_list))]
    makeWord(0, len(ch_list)-1)
