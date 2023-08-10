class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        frq = {i : [strs[i].count('0'), strs[i].count('1')] for i in range(len(strs))}
        dp = set()
        dp.add((0,0,0))
        ans = 0
        
        for i in range(len(strs)-1,-1,-1):
            nextDp = set()
            for t in dp:
                if t[0] + frq[i][0] <= m and t[1] + frq[i][1] <= n:
                    nextDp.add((t[0] + frq[i][0],t[1] + frq[i][1],t[2] + 1))
                    
                    ans = max(ans, t[2] + 1)
            dp = dp.union(nextDp)
            
        return ans