class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def primeCalculate(num):
            st = set()
            i = 2
            while num >= i:
                if num % i == 0:
                    st.add(i)
                    num = num // i
                else:
                    i += 1
            return st
        
        ans = set()
        for num in nums:
            ans = ans.union(primeCalculate(num))
        
        return len(ans)
        