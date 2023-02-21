# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = slow = head
        while fast:
            fast = fast.next.next
            slow = slow.next
        cur = slow
        prev = None
        while cur:
            cur.next, prev,cur = prev,cur,cur.next
        
        maxx = 0
        while prev:
            maxx = max(maxx, prev.val + head.val)
            head = head.next
            prev = prev.next
        return maxx
        
        

            
            
            
            
            
            
            
            