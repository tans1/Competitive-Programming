# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res = []
        
        def dfs(root, cur):
            if root and not root.left and not root.right:
                res.append(cur + [str(root.val)])
                return
            
            elif root and (root.left or root.right):
                cur.append(str(root.val))
                dfs(root.left, cur)
                
                
                dfs(root.right, cur)
                cur.pop()

        
        dfs(root, [])
        # print(res)
        ans = list(map(lambda x: '->'.join(x), res))
        
        return ans
        