class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        inDegree = [0 for i in range(n)]
        for u,v in edges:
            inDegree[v] += 1
        res = []
        for i in range(n):
            if inDegree[i] == 0:
                res.append(i)
        return res