class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def helper(nm,lst):
            for n in lst:
                if n == 0 or nm % n != 0:
                    return False
            return True
                
        ans = []
        for nm in range(left, right+1):
            lst = list(map(int,list(str(nm))))
            
            if helper(nm,lst):
                ans.append(nm)
        return ans
            