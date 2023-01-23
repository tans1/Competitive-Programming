# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        dummy = tail = ListNode(-1)
        for n in lists:
            node = n
            while node:
                temp.append(node.val)
                node = node.next
        temp.sort()
        for n in temp:
            tail.next = ListNode(n)
            tail = tail.next
            
        return dummy.next