# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        node = head
        length = 1
        while node.next:
            node = node.next
            length += 1 
        node.next = head  #lets make it cyclic
        
        k= length - (k % length)  #go to the last k nodes
        while k > 0:
            node = node.next
            k -= 1

        
        newhead = node.next  #since it is cyclic the last node is related to the first
        node.next = None
        return newhead