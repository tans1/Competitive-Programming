class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        for i in range(97,123):
            char = chr(i)
            temp = float('inf')
            
            for wrd in words:
                fr = wrd.count(char)
                temp = min(temp, fr)
            
            res.extend([char]*temp)
            
        return res
        