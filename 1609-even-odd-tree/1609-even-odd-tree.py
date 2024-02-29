# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        q.append((root, 0))
        prev = 2
        
        while q:
            nd, lvl = q.popleft()
            if lvl % 2 == 0: # even level
                if nd.val % 2 == 0:
                    return False
                if prev % 2 != 0 and prev >= nd.val:
                    return False
                
            else: # odd level
                if nd.val % 2 != 0:
                    return False
                if prev % 2 == 0 and prev <= nd.val:
                    return False
            prev = nd.val
            
            if nd.left:
                q.append((nd.left, lvl + 1))
            if nd.right:
                q.append((nd.right, lvl + 1))
                    
            
        return True