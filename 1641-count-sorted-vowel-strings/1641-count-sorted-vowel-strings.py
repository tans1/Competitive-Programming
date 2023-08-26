class Solution:
    def countVowelStrings(self, n: int) -> int:
        vowels = ['a','e','i','o','u']
        ans = 0
        
        @lru_cache
        def dfs(i,cur):
            nonlocal ans
            if len(cur) == n:
                ans += 1
                return
            for j in range(i,len(vowels)):
                dfs(j,cur + vowels[j])
        dfs(0,"")
        return ans