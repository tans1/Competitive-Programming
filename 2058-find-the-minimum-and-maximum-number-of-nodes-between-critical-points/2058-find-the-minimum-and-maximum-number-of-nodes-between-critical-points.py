# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev , node = head , head.next
        dst = []
        cnt = 2
        while node.next:
            if prev.val < node.val and node.val > node.next.val:
                dst.append(cnt)
            elif prev.val > node.val and node.val < node.next.val:
                dst.append(cnt)
            cnt += 1
            node = node.next
            prev = prev.next
        if len(dst) > 1:
            minn = float('inf')
            for i in range(len(dst)-1):
                minn = min(minn, dst[i+1] - dst[i])
            return [minn, dst[-1]-dst[0]]
        else:
            return [-1,-1]