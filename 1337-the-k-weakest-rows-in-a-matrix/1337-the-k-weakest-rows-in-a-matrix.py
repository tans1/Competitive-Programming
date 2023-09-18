class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        for i in range(len(mat)):
            mat[i].append(i+10)
        temp2 = sorted(mat,key = lambda x: (x.count(1), x[-1]))
        
        ans = []
        for i in range(k):
            ans.append(temp2[i][-1]-10)
        return ans
        
