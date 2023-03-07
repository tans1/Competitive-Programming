# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def helper(root,temp):
            if root:
                helper(root.left,temp)
                temp.append(root.val)
                helper(root.right, temp)
            return temp
        
        res = helper(root,[])
        return res[k-1]