class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res = []
        
        for i in range(97,123):
            char = chr(i)
            temp = []
            for wrd in words:
                fr = wrd.count(char)
                temp.append(fr)
                
            res.extend([char]*min(temp))
            
        return res
        