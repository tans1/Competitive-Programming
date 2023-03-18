class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        dct = {
            "2" : ["a","b","c"],
            "3" : ["d","e","f"],
            "4" : ["g","h","i"],
            "5" : ["j","k","l"],
            "6" : ["m","n","o"],
            "7" : ["p","q","r","s"],
            "8" : ["t","u","v"],
            "9" : ["w","x","y","z"]
        }
        
        res = []
        def backtracking(i,cur):
            if len(cur) == len(digits):
                res.append("".join(cur[::]))
                return
            
            for l in dct[digits[i]]:
                cur.append(l)    
                backtracking(i+1, cur)
                
                cur.pop()
        
        backtracking(0,[])                
        return res
            
            
        