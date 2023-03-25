# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # first find the level order traversal and reverse some of it
        dct = {}
        
        def dfs(root,level):
            if root:
                if level not in dct:
                    dct[level] = []
                dct[level].append(root.val)
                
                dfs(root.left, level + 1)
                dfs(root.right, level + 1)
        dfs(root, 1)
        temp = sorted(dct.items())
        
        res = []
        for k, v in dct.items():
            if k % 2 == 0:
                v.reverse()
            res.append(v)
        return res