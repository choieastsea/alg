# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # merge sort
        current = head
        length = 0
        pointList = []
        while current is not None:
            pointList.append(current)
            current = current.next
            length += 1
        if length == 0:
            return head
        pointList.sort(key=lambda x:x.val)
        head = pointList[0]
        current = head
        for i in range(1,length):
            # 순서대로 연결
            # print(current.val)
            current.next = pointList[i]
            current = pointList[i]
        current.next = None
        return head