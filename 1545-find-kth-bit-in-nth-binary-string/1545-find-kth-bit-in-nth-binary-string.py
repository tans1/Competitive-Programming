class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def recursive(n):
            if n == 1:
                return ["0"]
            
            up =  recursive(n-1) 
            
            temp = up.copy()
            for i in range(len(temp)):
                if temp[i] == "1":
                    temp[i] = "0"
                else:
                    temp[i] = "1"
            temp.reverse()
            
            return up + ["1"] + temp
        
        res = recursive(n)
        
        return res[k-1]