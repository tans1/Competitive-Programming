# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.i = 0
        
        def helper(root):
          if root:
            helper(root.left)
            self.stack.append(root.val)
            helper(root.right)
          
        helper(root)
        self.length = len(self.stack)
        
    def next(self) -> int:
      self.i += 1
      return self.stack[self.i-1]

    def hasNext(self) -> bool:
        return self.i < self.length


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()