class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dct = {stones[i]:set() for i in range(len(stones))}
        dct[0].add(0)

        for i,v in enumerate(stones):
            for k in dct[v]:
                opt1 = v + (k-1)
                opt2 = v + k
                opt3 = v + (k+1)
                
                if opt1 > v and opt1 in dct:
                    dct[opt1].add(k-1)
                if opt2 > v and opt2 in dct:
                    dct[opt2].add(k)
                if opt3 > v and opt3 in dct:
                    dct[opt3].add(k+1)
                
                if opt1 == stones[-1] or opt2 == stones[-1] or opt3 == stones[-1]:
                    return True
        return False
                
                