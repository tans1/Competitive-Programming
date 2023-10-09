class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # use Rabin - Carbin
        if len(haystack) < len(needle):
            return -1
        al = 27
        powers = [((al**i))for i in range(len(haystack))]
        
        needle_ = 0
        haystack_ = 0
        for i in range(len(needle)-1,-1,-1):
            needle_ += (ord(needle[i]) - 96)*powers[len(needle) -i-1]
            haystack_ += (ord(haystack[i]) - 96)*powers[len(needle) -i-1]
        
        if haystack_ == needle_:
            return 0
        for i in range(len(needle),len(haystack)):
            
            poll = (ord(haystack[i-len(needle)])-96)*powers[len(needle)-1]
            
            res = haystack_ - poll
            
            haystack_ = res*al + (ord(haystack[i]) - 96)
            if haystack_ == needle_:
                return i - len(needle) + 1
        return -1
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        # for i in range(len(haystack)):
        #     for j in range(len(needle)):
        #         if i+j < len(haystack) and haystack[i+j] != needle[j]:
        #             break
        #     if i+j < len(haystack)  and haystack[i+j] == needle[j] and j + 1 == len(needle):
        #         return i
        # return -1