# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        
        if len(preorder) == 1:
            return root
        
        def insertNode(root, num):
            if num < root.val:
                if root.left:
                    insertNode(root.left, num)
                else:
                    root.left = TreeNode(num)

            elif num > (root.val):
                if root.right:
                    insertNode(root.right, num)
                else:
                    root.right = TreeNode(num)
            return
        
        for i in range(1, len(preorder)):
            insertNode(root, preorder[i])
        
        return root
        
            
            
            
                
            
            