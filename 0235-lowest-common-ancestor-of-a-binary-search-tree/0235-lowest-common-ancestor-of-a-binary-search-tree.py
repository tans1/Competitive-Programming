# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def pathTracker(root, stack,req):
            if root:
                if root.val == req:
                    stack.append(root.val)
                    return stack
                
                elif req > root.val :
                    stack.append(root.val)
                    return pathTracker(root.right, stack,req)
                
                elif req < root.val:
                    stack.append(root.val)
                    return pathTracker(root.left, stack,req)
            
        pathP = pathTracker(root, [],p.val)
        pathQ = pathTracker(root, [],q.val)
        
        res = pathP[0]
        
        for i in range(min(len(pathP), len(pathQ))):
            if pathP[i] == pathQ[i]:
                res = pathP[i]
        return TreeNode(res)
        
                
                