from heapq import heappush, heappop
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        """
        정렬된 nums1과 nums2에서 하나씩 골라서 쌍을 만들 때, (a1,a2)의 합이 가장 작은 k개 뽑는다
        """
        heap = [] # (합, (el1, el2))
        maxVal = -10**10
        for n1 in nums1:
            for n2 in nums2:
                # print(n1,n2,maxVal)
                if maxVal >= -n1 - n2:
                    break
                heappush(heap, [-n1-n2, (n1,n2)]) # min-heap, n1+n2의 합이 크면 나가야하므로 heap의 앞에 위치해야함
                if len(heap) > k:
                    maxVal = heappop(heap)[0] # 가장 작은 것 없애준다 == 합이 가장 큰 것
        result = []
        for i in range(len(heap)):
            result.append(heap[i][1])
        return result