from heapq import heappush, heappop
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
            if len(heap) > k:
                # k개로 heap 유지
                heappop(heap) # 가장 작은 것 탈락
        # print(heap)
        return heappop(heap)