class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        mat = [[(float("inf"),1) for _ in range(40)] for _ in range(40)]
        dct = {}
        cnt = 0
        
        for i in range(len(equations)):
            x,y = equations[i]
            cst = values[i]
            if x not in dct:
                dct[x] = cnt
                cnt += 1
            if y not in dct:
                dct[y] = cnt
                cnt += 1
            mat[dct[x]][dct[y]] = (cst,1)
            mat[dct[y]][dct[x]] = (1,cst)
        
        for k in range(26):
            for i in range(26):
                for j in range(26):
                    prvx, prvy = mat[i][j]
                    temp1x, temp1y = mat[i][k]
                    temp2x, temp2y = mat[k][j]
                    
                    if (prvx / prvy) > ((temp1x*temp2x) / (temp1y*temp2y)):
                        mat[i][j] = (temp1x*temp2x, temp1y*temp2y)
                    
        
        ans = []
        for x,y in queries:
            if x not in dct or y not in dct:
                ans.append(-1)
            else:
                valx, valy = mat[dct[x]][dct[y]]
                if valx / valy == float("inf"):
                    ans.append(-1)
                else:
                    ans.append(valx / valy)
        return ans
            