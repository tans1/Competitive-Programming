class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        st = set(nums)
        
        for i in range(n):
            rev = list(str(nums[i]))
            rev.reverse()
            st.add(int(''.join(rev)))
        
        return len(st)