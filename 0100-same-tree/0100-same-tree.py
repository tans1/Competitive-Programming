# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def helper(p,q):
            if not p and not q:
                return True
            
            if p and q and p.val != q.val:
                return False
            
            elif (p and not q) or (q and not p):
                return False
            
            
            else:
                return helper(p.left, q.left) and helper(p.right, q.right)
            
        
        return helper(p,q)
                
        