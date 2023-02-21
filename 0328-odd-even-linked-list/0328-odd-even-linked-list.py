# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = tail = ListNode(-1)
        node1 = head
        node2 = head.next
        while node1:
            v = node1.val
            tail.next = ListNode(v) 
            tail = tail.next
            if node1.next:
                node1 = node1.next.next
            else:
                break
        while node2:
            v = node2.val
            tail.next = ListNode(v)
            tail = tail.next
            if node2.next:
                node2 = node2.next.next
            else:
                break
        return dummy.next