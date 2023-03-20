# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        
        
        def backtracking(root,cur, sm):  # traverse till the leaf node and keep the sum and list of the nodes along the sum, if sum == target, return it
            if root and not root.left and not root.right:
                if sm + root.val == targetSum:
                    res.append(cur + [root.val])
                    return
                    
            elif root:
                cur.append(root.val)
                
                backtracking(root.left,cur, sm + root.val)
                
                backtracking(root.right,cur, sm + root.val)
                cur.pop()

                
                
        backtracking(root,[], 0)
        return res
                    
                