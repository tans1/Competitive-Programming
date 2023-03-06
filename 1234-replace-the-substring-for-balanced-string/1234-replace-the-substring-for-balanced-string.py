class Solution:
    def balancedString(self, s: str) -> int:
        frq = Counter(s)
        n = len(s)
        ans = float('inf')
        
        if (frq['Q'] == n / 4) and (frq['W'] == n / 4) and  (frq['E'] == n / 4) and  (frq['R'] == n / 4 ):
            return 0
        
        required = []
        
        for k, v in frq.items():
            if v > ( n/4 ):
                required.append([k , v - (n / 4)])
                
        r = 0
        l = 0
        wnd = defaultdict(int)
        
        while l < n and r < n:
            wnd[s[r]] += 1
            
            if len(required) == 1:
                while l <= r and required[0][1] <= wnd[required[0][0]]:
                    ans = min(ans, r-l+1)
                    wnd[s[l]] -= 1
                    l += 1
            
            elif len(required) == 2:
                 while l <= r and required[0][1] <= wnd[required[0][0]] and required[1][1] <= wnd[required[1][0]]:
                    ans = min(ans, r-l+1)
                    wnd[s[l]] -= 1
                    l += 1
            
            elif len(required) == 3:
                while l <= r and required[0][1] <= wnd[required[0][0]] and required[1][1] <= wnd[required[1][0]] and required[2][1] <= wnd[required[2][0]]:
                    ans = min(ans, r-l+1)
                    wnd[s[l]] -= 1
                    l += 1
            r += 1
        return ans