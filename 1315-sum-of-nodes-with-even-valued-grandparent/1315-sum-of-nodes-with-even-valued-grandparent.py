# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(root):
            if root:
                if root.val % 2 == 0:
                    if root.left:
                        if root.left.left: self.ans += root.left.left.val ;
                        if root.left.right: self.ans += root.left.right.val ;
                    
                    if root.right:
                        if root.right.left: self.ans += root.right.left.val ;
                        if root.right.right: self.ans += root.right.right.val ;
                    
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return self.ans