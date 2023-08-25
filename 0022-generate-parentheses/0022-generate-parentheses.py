class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def dfs(opn, close, cur):
            nonlocal ans
            if opn == close == 0:
                ans.append(cur)
                return
            
            if opn > 0:
                if opn == close:
                    dfs(opn-1,close,cur + "(")
                else:
                    dfs(opn-1,close,cur + "(")
                    dfs(opn,close-1,cur + ")")
            else:
                dfs(opn,close-1,cur + ")")
        
        dfs(n,n,"")
        return ans