# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dictionary = collections.defaultdict(ListNode)
        while(head):
            # print(dictionary)
            if head in dictionary:
                return True
            dictionary[head] = True
            head = head.next
        return False