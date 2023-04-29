# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(set)
        
        def dfs(node):
            if node:
                if node.left:
                    graph[node.val].add(node.left.val)
                    graph[node.left.val].add(node.val)
                    dfs(node.left)
            
            if node.right:
                    graph[node.val].add(node.right.val)
                    graph[node.right.val].add(node.val)
                    dfs(node.right)
        dfs(root)
        q = deque()
        q.append((target.val,0))
        visited = set()
        visited.add(target.val)
        
        while q:
            nd , lvl = q.popleft()
            if lvl == k:
                break
            
            for nb in graph[nd]:
                if nb not in visited:
                    q.append((nb,lvl+1))
                    visited.add(nb)  
        ans = []
        if lvl == k:
            ans.append(nd)
            for nod, level in q:
                ans.append(nod)
        
        return ans
            
                
            