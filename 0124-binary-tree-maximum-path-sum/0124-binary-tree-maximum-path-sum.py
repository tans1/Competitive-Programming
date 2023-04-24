# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = float('-inf')
        
        def dfs(node):
            nonlocal ans
            if node:
                # base case
                if not node.left:
                    left = 0
                else:
                    left = dfs(node.left)
                
                if not node.right:
                    right = 0
                else:
                    right = dfs(node.right)
                    
                ans = max(ans, left + node.val, right + node.val, left + right + node.val, node.val)
                return max(left + node.val, right + node.val, node.val)
        
        dfs(root)
        return ans
                
            