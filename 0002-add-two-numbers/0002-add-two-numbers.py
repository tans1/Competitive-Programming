# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = tail = ListNode(-1)
        carry = 0
        while l1 and l2:
            v = l1.val + l2.val + carry
            tail.next = ListNode(v % 10)
            tail = tail.next
            carry = 1 if v != (v%10) else 0
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            v = l1.val + carry
            tail.next = ListNode(v % 10)
            tail = tail.next
            carry = 1 if v != (v%10) else 0
            l1 = l1.next
    
        while l2:
            v = l2.val + carry
            tail.next = ListNode(v % 10)
            tail = tail.next
            carry = 1 if v != (v%10) else 0
            l2 = l2.next
            
        if carry != 0:
            tail.next = ListNode(carry)
            tail = tail.next
            
        return dummy.next
    