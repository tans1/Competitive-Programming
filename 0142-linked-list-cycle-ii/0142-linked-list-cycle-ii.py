# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return 
        dct = defaultdict(int)
        node = head
        while node:
            if node in dct:
                return dct[node]
            dct[node] = node
            node = node.next
        return 
    
#         slow = head
#         fast = head
        
#         while fast and fast.next:
#             if fast != head and fast == slow:
#                 break
#             fast = fast.next.next
#             slow = slow.next
#         if fast == slow:
            
            