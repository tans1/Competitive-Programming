class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if s == t: return t
        
        n = len(s)
        m = len(t)
        frq_t = Counter(t)
        frq_f = defaultdict(int)
        l = 0
        valid = 0
        gap = n
        ans = ""
        
        for r in range(n):
            frq_f[s[r]] += 1
            
            if s[r] in frq_t and  frq_t[s[r]] == frq_f[s[r]]:
                valid += 1
            while valid >= len(frq_t) and l <= r:
                
                if (r-l +1) <= gap:
                    ans = s[l:r+1]
                    gap = r - l + 1
                
                if s[l] in frq_t and frq_f[s[l]] <= frq_t[s[l]]:
                    valid -= 1

                frq_f[s[l]] -= 1
                l += 1
        
        return ans
                    
                    
            