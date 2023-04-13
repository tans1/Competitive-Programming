# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #we can apply bubble sort for small number of linked list
        #curr = head
        #while curr:
            #nxt = curr.next
            #while nxt:
                #if curr.val > nxt.val:
                    #curr.val , nxt.val = nxt.val, curr.val
                #nxt = nxt.next
            #curr = curr.next
        #return head
###############################################################################################
########### USING MERGE SORT
        if not head or not head.next: return head

        # cut the list into two halves
        slow,fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)

        return self.merge(l, r)

    def merge(self, l, r):
        if l is None:
            return r
        elif r is None:
            return l

        dummy = tail = ListNode(-1)

        while l and r:
            if l.val <= r.val:
                tail.next = l
                l = l.next
            else:
                tail.next = r
                r = r.next
            tail = tail.next

        tail.next = l if r is None else r
        return dummy.next

#######################################################
        
################  USING STACK

        #newLinkedList = pointer = ListNode(0) 
        #node = head
        #stack = []
        #while node:
         #   stack.append(node.val)
          #  node = node.next
        #stack.sort()
        #for num in stack:
         #   pointer.next = ListNode(num)
          #  pointer = pointer.next
        #return newLinkedList.next
        
        

        