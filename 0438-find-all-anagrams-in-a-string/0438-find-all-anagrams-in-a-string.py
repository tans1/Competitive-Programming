class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:      
        res = []
        fr = Counter(p)
        size = len(p)
        windowCount = Counter(s[:size])
        
        if windowCount == fr:
            res.append(0)
        
        for i in range(size, len(s)):
            windowCount[s[i-size]] -= 1
            if not windowCount[s[i-size]]:
                windowCount.pop(s[i-size])
                
            if s[i] in windowCount:
                windowCount[s[i]] += 1
                
            else:
                windowCount[s[i]] = 1
                
            
            if windowCount == fr:
                res.append(i-size+1)
                
                
        return res
                
                