# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return head
        dummy = tail = ListNode(-1)
        odd = head
        even = head.next
        while odd:
            tail.next = ListNode(odd.val)
            tail = tail.next
            if odd.next:
                odd = odd.next.next
            else:
                break
        while even:
            tail.next = ListNode(even.val)
            tail = tail.next
            if even.next:
                even = even.next.next
            else:
                break
        return dummy.next
