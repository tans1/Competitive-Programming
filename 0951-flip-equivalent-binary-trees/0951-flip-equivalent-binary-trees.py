# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if (not root1 and root2) or (root1 and not root2) or (root1 and root2 and root1.val != root2.val):
            return False
        if not root1 and not root2:
            return True
        ans = True
        def dfs(rt1, rt2):
            nonlocal ans
            if rt1 and rt2:
                if rt1.left and rt1.right and rt2.left and rt2.right:
                    if rt1.left.val == rt2.left.val and rt1.right.val == rt2.right.val:
                        dfs(rt1.left, rt2.left)
                        dfs(rt1.right, rt2.right)
                    elif rt1.left.val == rt2.right.val and rt1.right.val == rt2.left.val:
                        temp = rt1.left
                        rt1.left = rt1.right
                        rt1.right = temp
                        dfs(rt1.left, rt2.left)
                        dfs(rt1.right, rt2.right)
                    else:
                        ans = False
                        return
                elif rt1.left and rt1.right:
                    if not rt2.left or not rt2.right:
                        ans = False
                        return
                elif not rt1.left and not rt1.right:
                    if rt2.right or rt2.left:
                        ans = False
                        return
                elif not rt1.left and rt1.right:
                    if rt2.left and not rt2.right and rt1.right.val == rt2.left.val:
                        temp = rt1.left
                        rt1.left = rt1.right
                        rt1.right = temp
                        dfs(rt1.left, rt2.left)
                    elif not rt2.left and rt2.right and rt2.right.val == rt1.right.val:
                        dfs(rt1.right, rt2.right)
                    else:
                        ans = False
                        return
                elif rt1.left and not rt1.right:
                    if rt2.left and not rt2.right and rt1.left.val == rt2.left.val:
                        dfs(rt1.left, rt2.left)
                    elif not rt2.left and rt2.right and rt2.right.val == rt1.left.val:
                        temp = rt1.left
                        rt1.left = rt1.right
                        rt1.right = temp
                        dfs(rt1.right, rt2.right)
                    else:
                        ans = False
                        return
                
                
            
            
        dfs(root1, root2)
        return ans
            
                    
                        
                        
        