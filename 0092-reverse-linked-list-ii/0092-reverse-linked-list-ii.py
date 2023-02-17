# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        before = tail1 = ListNode(-1)
        rever = tail2 = ListNode(-1)
        after = tail3 = ListNode(-1)
        k = 1
        while k < left:  #before the revesed group
            tail1.next = ListNode(head.val)
            tail1 = tail1.next
            head = head.next
            k += 1
        while k <= right:  #the reversed group of list
            tail2.next = ListNode(head.val)
            tail2 = tail2.next
            head = head.next
            k += 1
        while head:  #after the reversed group
            tail3.next = ListNode(head.val)
            tail3 = tail3.next
            head = head.next
        ans = None
        rever = rever.next
        while rever:
            rever.next, ans, rever = ans, rever, rever.next
        after = after.next
        before = before.next
        result = tail4 = ListNode(-1)  #final answer
        while before:
            tail4.next = ListNode(before.val)
            tail4 = tail4.next
            before = before.next
        while ans:
            tail4.next = ListNode(ans.val)
            tail4 = tail4.next
            ans = ans.next
        while after:
            tail4.next = ListNode(after.val)
            tail4 = tail4.next
            after = after.next
        return result.next