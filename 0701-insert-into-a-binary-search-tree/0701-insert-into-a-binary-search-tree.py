# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(val)
        
        def helper(root,val):
            if not root:
                return TreeNode(val)
            
            if val < root.val :
                root.left = helper(root.left,val)
            else:
                root.right = helper(root.right,val)
            return root
        
        
        return helper(root,val)