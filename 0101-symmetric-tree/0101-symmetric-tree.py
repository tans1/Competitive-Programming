# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        dct = defaultdict(list)
        
        def helper(root, order):
            if root:
                dct[order].append(root.val)
                helper(root.left, order + 1)
                helper(root.right, order + 1)
            else:
                dct[order].append(None)
            
        helper(root,0)
        
        for key, value in dct.items():
            if len(value) > 1:
                i = 0
                j = len(value)-1

                while i <= j and value[i] == value[j]:
                    i += 1
                    j -= 1

                if value[i] != value[j]:
                    return False
        return True