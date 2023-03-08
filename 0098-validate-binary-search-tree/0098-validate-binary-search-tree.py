# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, stack):
            if root:
                helper(root.left, stack)
                stack.append(root.val)
                helper(root.right, stack)
            
            return stack
        
        res = helper(root, [])
        temp = sorted(res)
        temp2 = Counter(res)
        
        if len(temp2) != len(res):
            return False
        
        return res == temp