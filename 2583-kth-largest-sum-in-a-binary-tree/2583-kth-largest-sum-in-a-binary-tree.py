# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        dct= defaultdict(int)
        
        def helper(root,level):
          if root:
            dct[level] += root.val

            helper(root.left, level + 1)
            helper(root.right, level + 1)
          
        helper(root, 1)
        vl = list(dct.values())
        vl = sorted(vl,reverse = True)
        
        
        if k > len(vl):
          return -1
        return vl[k-1]
