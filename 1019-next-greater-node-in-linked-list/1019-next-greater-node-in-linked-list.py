# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        node1 = node2 = head
        len_list = 0 
        while node1:
            len_list += 1
            node1 = node1.next
            
        res = [0] * len_list 
        i , stack = 0, []
        while node2:
            while len(stack) > 0 and node2.val > stack[-1][0]:
                a = stack.pop()
                res[a[1]] = node2.val
            stack.append([node2.val,i])
            i += 1
            node2 = node2.next
        return res