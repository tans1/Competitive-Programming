# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        dct = defaultdict(list)
        
        def helper(root,order):
            if root:
                dct[order].append(root.val)
                helper(root.left,order+1)
                helper(root.right,order+1)
        
        helper(root,0)
        
        res = []
        for k, v in dct.items():
            res.append(v)
        return res