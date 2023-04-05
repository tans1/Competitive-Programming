class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        temp = []
        cost = 0
        
        for n in instructions:
            l = bisect_left(temp, n)
            r = bisect_right(temp, n)
            
            if r < len(temp):
                mx = len(temp) - r 
            else:
                mx = 0
            cost += min(l,mx)
            insort(temp,n)
        return cost % (10**9 + 7)