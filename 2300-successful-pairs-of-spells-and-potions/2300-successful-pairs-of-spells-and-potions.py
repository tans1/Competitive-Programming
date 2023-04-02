class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        n = len(potions)
        
        for s in spells:
            
            x = success // s
            if success % s != 0:
                x += 1
            
            i = bisect_left(potions, x)
            
            if i < n:
                temp = n - i
                if potions[i] < x:
                    temp -= 1
            else:
                temp = 0
                
            ans.append(temp)
        return ans
                
                