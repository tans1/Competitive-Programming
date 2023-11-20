# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        sm = 0
        def dfs(node):
            nonlocal sm
            if node:
                if node.left:
                    # check if it is left leaf node
                    if not node.left.left and not node.left.right:
                        sm += node.left.val
                    dfs(node.left)
                if node.right:
                    dfs(node.right)
        
        dfs(root)
        return sm
                    
        