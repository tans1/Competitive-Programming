# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.string = ""
        def dfs(root):
            if not root:
                return
            self.string += str(root.val)
            if not root.left and not root.right:
                return
            self.string += "("
            dfs(root.left)
            self.string += ")"
            
            if root.right:
                self.string += "("
                dfs(root.right)
                self.string += ")"
        dfs(root)
        return self.string