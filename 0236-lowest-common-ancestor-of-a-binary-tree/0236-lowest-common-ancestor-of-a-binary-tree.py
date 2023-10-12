# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def pathFinder(rt, node):
            if rt:
                if rt.val == node:
                    return [True, [rt.val]]
                if rt.left:
                    left = pathFinder(rt.left, node)
                    if left and left[0]:
                        left[1].append(rt.val)
                        return left
                if rt.right:
                    right = pathFinder(rt.right, node)
                    if right and right[0]:
                        right[1].append(rt.val)
                        return right
        
        res = -1
        def dfs(rt,node):
            nonlocal res
            if rt:
                if rt.val == node:
                    res = rt
                    return
                if rt.left:
                    dfs(rt.left, node)
                if rt.right:
                    dfs(rt.right, node)
                    
        _, path1 = pathFinder(root,p.val)
        _, path2 = pathFinder(root,q.val)
        
        path1.reverse()
        path2.reverse()
        ans = -1
        for i in range(min(len(path1),len(path2))):
            if path1[i] == path2[i]:
                ans = path1[i]
            else:
                break
        dfs(root, ans)
        return res
        
        