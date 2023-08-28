# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        up = 0
        head = None
        current = head
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            val = (val1 + val2 + up)%10
            up = (val1 + val2 + up)//10
            print(val1, val2, val, up)
            new_node = ListNode(val)
            if head is None:
                head = new_node
                current = head
            else:
                # 기존 링크드 리스트에 추가
                current.next = new_node
                current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if up == 1:
            # 마지막 하나 남은 경우
            current.next = ListNode(1)
        return head
