# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        rev = None
        node = head
        dummy = tail = ListNode(-1)
        while node:
            tail.next = ListNode(node.val)
            tail = tail.next
            node.next, rev, node = rev, node, node.next
        
        temp = dummy.next
        while temp:
            if temp.val == rev.val:
                temp = temp.next
                rev = rev.next
            else:
                return False
        return True
