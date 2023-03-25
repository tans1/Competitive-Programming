# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # after swapping , the inorder == sorted(inorder), so find the error causing and swap it
        temp1 = []
        def dfs(root):
            if root:
                dfs(root.left)
                temp1.append(root.val)
                dfs(root.right)
        dfs(root)
        
        temp2 = sorted(temp1)
        
        for i in range(len(temp1)):
            if temp1[i] != temp2[i]:
                break
        def correcting(root):
            if root:
                if root.val == temp1[i]:
                    root.val = temp2[i]
                
                elif root.val == temp2[i]:
                    root.val = temp1[i]
                
                correcting(root.left)
                correcting(root.right)
        
        correcting(root)