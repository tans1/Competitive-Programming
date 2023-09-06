# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        exact, remainder = n // k, n % k
        result = []
        
        while head:
            tempCount = 0
            dummy = None  
            while head and tempCount < exact:
                if dummy is None:
                    dummy = ListNode(head.val)
                    tail = dummy
                else:
                    tail.next = ListNode(head.val)
                    tail = tail.next
                    
                head = head.next
                tempCount += 1
                
            if remainder > 0 and head:
                if dummy is None:
                    dummy = ListNode(head.val)
                    tail = dummy
                else:
                    tail.next = ListNode(head.val)
                    tail = tail.next
                    
                head = head.next
                remainder -= 1
            result.append(dummy)
        
        for _ in range(k - n):
            result.append(None) 
        
        return result
