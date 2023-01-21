# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pointer1 = pointer2 = head
        dummy = tail = ListNode(-1)
        
        while pointer1 and pointer2:
            if pointer1.val == 0:
                res = 0
                if pointer2.val == 0:
                    pointer2 = pointer2.next
                while pointer2 and pointer2.val != 0:
                    res += pointer2.val
                    pointer2 = pointer2.next
                
                tail.next = ListNode(res)
                tail = tail.next
                
            pointer1 = pointer1.next
            if pointer2 == pointer1:
                pointer2 = pointer2.next
        return dummy.next