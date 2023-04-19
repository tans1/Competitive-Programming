class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        subsets = []

        def backtrack(i , cur):
            if i >= len(nums):
                subsets.append(cur[:])
                return
            
            cur.append(nums[i])
            backtrack(i +1 , cur)
            
            cur.pop()
            backtrack(i + 1 , cur)
            
        backtrack(0,[])
        mxBit = nums[0]
        for n in nums:
            mxBit = mxBit | n
        
        ans = 0
        for st in subsets:
            if st:
                btOr = st[0]
                for n in st:
                    btOr = btOr | n
                if btOr == mxBit:
                    ans += 1
        return ans
        
