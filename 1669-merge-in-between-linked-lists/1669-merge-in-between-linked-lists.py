# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1
        cnt = 1
        # if node.val != a: #not at the beginning 
        while node:
            if node.next and cnt == a:
                left = node
            if cnt == b:
                right = node.next
            node = node.next
            cnt += 1
        left.next = list2
        while left.next:
            left = left.next
        left.next = right.next
        return list1
        # else:
        #     while node:
        #         if node.val == b:
        #             right = node.next
        #         node = node.next
        #     node2 = list2
        #     while node2.next:
        #         node2 = node2.next
        #     node2.next = right
        #     return list2
        
            
        