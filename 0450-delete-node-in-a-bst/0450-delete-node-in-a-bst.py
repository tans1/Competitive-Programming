# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        def helper(root, key):
            if not root:
                return None
            
            if root.val < key:
                root.right = helper(root.right, key)
            
            elif root.val > key:
                root.left = helper(root.left, key)
            
            else: #now the node to be deleted is found  root.val = key
                if not root.left and not root.right:
                    root = None
                    return root
                
                elif root.right and not root.left:
                    return root.right
                
                elif root.left and not root.right:
                    return root.left
                
                else: # if it has two childs
                    
                    temp = root.right
                    
                    while temp.left:
                        temp = temp.left

                    root.val = temp.val
                    root.right = helper(root.right, temp.val)
                        
            return root
        return helper(root, key)
                