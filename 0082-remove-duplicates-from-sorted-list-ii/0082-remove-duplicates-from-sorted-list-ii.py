# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head : return
        dummy  = tail = ListNode(-1)
        tail.next = head
        # tail = dummy
        
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                tail.next = head.next
            else:
                if tail :
                    tail = tail.next
            head = head.next
        return dummy.next

