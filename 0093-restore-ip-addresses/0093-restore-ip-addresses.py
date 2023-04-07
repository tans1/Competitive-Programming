class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        if len(s) > 12:
            return res
        
        def backtracking(i, dots, curIp):
            if dots == 4 and i == len(s):
                res.append(curIp[:-1])
                return
            
            if dots > 4:
                return 
            
            for j in range(i, min(i+3, len(s))):
                if int(s[i:j+1]) <= 255 and (len(str(int(s[i:j+1])))) == len(s[i:j+1]):
                    backtracking(j+1, dots+1, curIp + s[i:j+1] + ".")
                
        backtracking(0,0,"")
        return res