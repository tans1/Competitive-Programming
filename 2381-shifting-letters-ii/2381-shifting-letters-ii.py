class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        temp = [0 for _ in range(len(s) + 1)]
        n = len(s)
        
        for shift in shifts:
            if shift[2] == 1:
                temp[shift[0]] += 1
                temp[shift[1] + 1] += -1
            else:
                temp[shift[0]] += -1
                temp[shift[1] + 1] += 1
                
            
        for i in range(1,n):
            temp[i] += temp[i-1]
        
        ls = list(s)
        for i , v in enumerate(ls):
            temp2 = ord(v) + temp[i]
            while temp2 < 97:
                temp2 += 26
            while temp2 > 122:
                temp2 -= 26
            
            ls[i] = chr(temp2)
        
        return "".join(ls)
            