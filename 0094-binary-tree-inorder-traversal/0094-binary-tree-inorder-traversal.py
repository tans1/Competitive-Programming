# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output =[]
        def inorderTr(root):
            if root:
                inorderTr(root.left)  
                output.append(root.val)
                inorderTr(root.right)
                
        inorderTr(root)
        return output
        
######################### THIS ALSO WORKS ############################################################        
        
        # current = root
        # stack = []
        # while (current or stack):
        #     while current:
        #         stack.append(current)
        #         current = current.left
        #     current = stack.pop()
        #     output.append(current.val)
        #     current = current.right
        # return output
        
                
         