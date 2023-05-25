class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        dct = defaultdict(int)
        
        for bill in bills:
            if bill == 10:
                if dct[5] == 0:
                    return False
                dct[5] -= 1
            elif bill == 20:
                if dct[5] > 0 and dct[10] > 0:
                    dct[5] -= 1
                    dct[10] -= 1
                    
                elif dct[5] >= 3:
                    dct[5] -= 3
                    
                elif (dct[5] == 0 and dct[10] == 0) or (dct[5] < 3):
                    return False
                
                
                
            dct[bill] += 1
        return True