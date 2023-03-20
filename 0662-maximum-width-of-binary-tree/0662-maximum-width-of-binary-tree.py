# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queu = deque([(root,0)])
        maxWidth = 1
        
        while queu:
            
            maxWidth = max(maxWidth,queu[-1][1] - queu[0][1]  + 1)
            
            
            for i in range(len(queu)):
                curNode, pos = queu.popleft()
                
                if curNode.left:
                    queu.append((curNode.left, 2 *pos))
                    
                if curNode.right:
                    queu.append((curNode.right, 2 * pos + 1 ))
            
            
        return maxWidth
                
                    
            
            