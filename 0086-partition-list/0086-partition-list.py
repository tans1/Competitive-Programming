# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = tail = ListNode(0)
        
        head1 = head2 = head
        while head1:
            if head1.val < x:
                tail.next = ListNode(head1.val)
                tail = tail.next
            head1 = head1.next
        while head2:
            if head2.val >= x:
                tail.next = ListNode(head2.val)
                tail = tail.next
            head2 = head2.next
        return dummy.next     
