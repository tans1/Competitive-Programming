# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        
        def helper(root):
            if not root.left and not root.right:
                self.cnt += 1
                return root.val , 1
            
            if root.right:
                smr, nmr = helper(root.right)
                
            if root.left:
                sml, nml = helper(root.left)
                
            if root.left and root.right:
                summ = (smr + sml + root.val)
                num = (nml + nmr + 1)
                    
            elif root.left:
                summ = sml + root.val
                num = 1 + nml
                
            elif root.right:
                summ = smr + root.val
                num = 1 + nmr
                
            if (summ // num) == root.val:
                self.cnt += 1

            return summ, num
        
        helper(root)
        return self.cnt
                
            
            
            
            