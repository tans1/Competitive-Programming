class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        
        if len(pattern) != len(s):
            return False
       
        dct = {}
        i = j = 0
        
        while i < len(pattern) and j < len(s):
            if pattern.count(pattern[i]) != s.count(s[j]) or (pattern[i] in dct and dct[pattern[i]] != s[j]):
                return False
            else:
                 dct[pattern[i]] = s[j]
            
            i += 1
            j += 1
            
        return True

            
                
            
        