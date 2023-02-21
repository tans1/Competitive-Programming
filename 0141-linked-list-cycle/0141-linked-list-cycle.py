# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: return False
        dct = defaultdict(bool)
        node = head
        while node:
            if dct[node]:
                return True
            dct[node] = True
            node = node.next
        return False
############################################################################################

        fast = slow =head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False