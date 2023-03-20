# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        dct = defaultdict(list)

        def traverse(level, root, i ):  # keep node in same column and incase there are multiple nodes, sort them by thir level
            if root:   
                dct[i].append([root.val, level])

                traverse( level + 1, root.left, i - 1)
                traverse( level + 1, root.right, i + 1)


        traverse(0, root, 0)
        temp = sorted(dct.items())
        res = []

        for nm in temp:
            if len(nm[1]) == 1:
                res.append([nm[1][0][0]])
            else:
                tmp = sorted(nm[1], key = lambda x:(x[1],x[0]))
                temp2 = []
                for j in tmp:
                    temp2.append(j[0])
                res.append(temp2)
        return res