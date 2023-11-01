# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        dct = defaultdict(int)
        def dfs(level, node):
            if node:
                dct[level] += node.val
                
                dfs(level + 1, node.left)
                dfs(level + 1, node.right)
        dfs(1,root)
        temp = sorted(dct.items(), key = lambda x: (x[1], -x[0]))
        return temp[-1][0]
                
        