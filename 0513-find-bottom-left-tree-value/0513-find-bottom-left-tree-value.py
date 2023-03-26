# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        dct = defaultdict(list)
        
        def dfs(root, level):
            if root:
                dct[level].append(root.val)
                
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        
        dfs(root, 1)
        
        temp = list(dct.keys())
        temp.sort()
        
        return dct[temp[-1]][0]