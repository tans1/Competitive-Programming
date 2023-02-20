# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next: return 
        # dct = defaultdict(int)
        # node = head
        # while node:
        #     if node in dct:
        #         return dct[node]
        #     dct[node] = node
        #     node = node.next
        # return 
    
        fast = slow =head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                node = head
                while node != fast:
                    node = node.next
                    fast = fast.next
                return fast
        return 

            
            