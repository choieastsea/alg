from sys import stdin

input = stdin.readline

def search(query):
    """
    A에 query가 있다면 1 없다면 0을 리턴
    """
    global A # 오름차순 정렬
    strt = 0
    end = len(A) - 1 # 마지막 인덱스!
    while strt <= end:
        mid = (strt + end) // 2
        # print(f'strt:{strt}, end:{end}, mid:{mid}')
        if A[mid] < query:
            strt = mid + 1
        elif A[mid] > query:
            end = mid - 1
        else:
            # 찾은 경우
            return 1
    return 0
    

if __name__ == "__main__":
    """
    정렬(nlogn) 이후 binary search(logn)으로 수행하는 것이 일일이 찾는 것보다 빠를 것
    """
    n = int(input())
    A = list(map(int, input().split()))
    # n sized A list에서 m개의 query(해당 숫자가 존재하는지)
    m = int(input())
    queries = list(map(int, input().split()))
    # 1. 정렬
    A.sort()
    # 2. BS
    for query in queries:
        print(search(query))