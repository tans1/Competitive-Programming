class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days == 1:
            return sum(weights)
        
        shipweight = [i for i in range(max(weights), sum(weights)+1)]
        n = len(weights)
        l , r = 0 , len(shipweight)-1
        
        res = float('inf')
        
        while  l <= r:
            md = (l + r) // 2
            shp = shipweight[md]
            sm , d = 0, 0
            
            for j in range(n):
                sm += weights[j]
                
                if sm == shp:
                    d += 1
                    sm = 0
                    
                elif sm > shp:
                    d += 1
                    sm = weights[j]
            
            if sm != 0:
                d += 1
                
            if d <= days:
                res = min(res, shp)
                r = md - 1
                
            elif d > days:
                l = md + 1

        return res
  