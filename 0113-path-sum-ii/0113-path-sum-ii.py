# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        def dfs(rt, curr, curr_sum):
            nonlocal ans
            if rt and not rt.left and not rt.right:
                if curr_sum + rt.val == targetSum:
                    temp = curr + [rt.val]
                    ans.append(temp)
                return
            if rt and  rt.left:
                curr.append(rt.val)
                dfs(rt.left, curr, curr_sum + rt.val)
                curr.pop()
            if rt and rt.right:
                curr.append(rt.val)
                dfs(rt.right, curr, curr_sum + rt.val)
                curr.pop()
                
                
        dfs(root, [], 0)
        return ans