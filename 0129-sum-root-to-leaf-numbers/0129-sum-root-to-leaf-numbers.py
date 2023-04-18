# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.sm = 0
        
        def dfs(root, cur):
            if root and not root.left and not root.right:
                self.sm += int(''.join(cur) + str(root.val))
                return
            
            cur.append(str(root.val))

            if root.left:
                dfs(root.left, cur)

            if root.right:
                dfs(root.right, cur)

            cur.pop()
            return
        
        dfs(root, [])
        
        return self.sm
                
                