class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        part = []
        memo = {}
        
        def checkPalindrome(i,j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
            
        def dfs(i):
            if i >= len(s):
                ans.append(part.copy())
                return
            for j in range(i,len(s)):
                if s[i:j+1] not in memo:
                    memo[s[i:j+1]] = checkPalindrome(i,j)
                
                if memo[s[i:j+1]]:
                    part.append(s[i:j+1])
                    dfs(j + 1)
                    part.pop()
        dfs(0)
        return ans