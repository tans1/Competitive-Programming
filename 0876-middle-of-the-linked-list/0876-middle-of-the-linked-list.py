# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        n = 0
        while node:
            n +=1
            node = node.next
            
        md = n // 2
        while md:
            head = head.next
            md -= 1
        return head

