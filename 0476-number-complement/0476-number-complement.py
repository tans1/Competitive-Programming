class Solution:
    def findComplement(self, num: int) -> int:
        temp = bin(num)
        ans = ""
        for i in range(2,len(temp)):
            if temp[i] == "1":
                ans += "0"
            else:
                ans += "1"
        
        return int(ans,2)
        