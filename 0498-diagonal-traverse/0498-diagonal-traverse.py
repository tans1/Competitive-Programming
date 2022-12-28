class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        
        row = len(mat)
        col = len(mat[0])
        
        for i in range(row):
            for j in range(col):
                dic[i+j].append(mat[i][j])
                
        temp = list(dic.values())
        i = 0
        while i < len(temp):
            temp[i].reverse()
            i += 2
        res = temp[0]
        for i in range(1,len(temp)):
            res.extend(temp[i])
        return res