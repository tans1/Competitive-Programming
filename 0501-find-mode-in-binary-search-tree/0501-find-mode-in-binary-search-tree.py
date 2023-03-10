# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        dct = defaultdict(int)
        
        def heleper(root):
            if root:
                dct[root.val] += 1
                heleper(root.left)
                heleper(root.right)
        
        heleper(root)
        
        frq = sorted(dct.items(), key = lambda x: -x[1])
        
        res = [frq[0][0]]
        i = 1
        n = len(frq)
        
        while i < n and frq[i][1] == frq[i-1][1]:
            res.append(frq[i][0])
            i += 1
        return res
        
                