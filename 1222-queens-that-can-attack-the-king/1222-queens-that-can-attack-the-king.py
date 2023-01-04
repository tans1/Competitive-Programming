class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        n = len(queens)
        
        preRow , postRow = [] , []
        preCol , postCol = [] , []
        preDiagOne , postDiagOne = [] , []
        preDiagTwo , postDiagTwo = [] , []
        
        for i in range(n):
            if queens[i][0] == king[0]:
                if queens[i][1] < king[1]:
                    preRow.append(queens[i])
                else:
                    postRow.append(queens[i])
                
            elif queens[i][1] == king[1]:
                if queens[i][0] < king[0]: 
                    preCol.append(queens[i])
                else:
                    postCol.append(queens[i])
            
            elif queens[i][0] - queens[i][1] == king[0]-king[1]:
                if (queens[i][0] + queens[i][1]) < (king[0] + king[1]):
                    preDiagOne.append(queens[i])
                else:
                    postDiagOne.append(queens[i])
                
            elif queens[i][0] + queens[i][1] == king[0]+king[1]:
                if (queens[i][0] - queens[i][1]) < (king[0]-king[1]):
                    preDiagTwo.append(queens[i])
                else:
                    postDiagTwo.append(queens[i])
                    
        res = []
        
        if len(preRow ) > 0:
            res.append(sorted(preRow, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        
        if len(postRow) > 0:
            res.append(sorted(postRow, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(preCol) > 0:
            res.append(sorted(preCol, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(postCol) > 0:
            res.append(sorted(postCol, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(preDiagOne) > 0:
            res.append(sorted(preDiagOne, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(postDiagOne) > 0:
            res.append(sorted(postDiagOne, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(preDiagTwo) > 0:
            res.append(sorted(preDiagTwo, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        if len(postDiagTwo) > 0:
            res.append(sorted(postDiagTwo, key=lambda x: abs(((x[0] - king[0])**2) + ((x[1] - king[1]) **2)))[0])
        
        
        return res
        