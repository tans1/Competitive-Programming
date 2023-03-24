# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        preSum = defaultdict(int)
        preSum[0] = 1
        self.count = 0
        
        def preorder(root,currSum,preSum):
            if root:
                currSum += root.val

                if (currSum - targetSum) in preSum:
                    self.count += preSum[currSum - targetSum]


                preSum[currSum] += 1


                preorder(root.left, currSum, preSum)
                preorder(root.right, currSum, preSum)

                preSum[currSum] -= 1
    
        
        preorder(root, 0, preSum);
        return self.count