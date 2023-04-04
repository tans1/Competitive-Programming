class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        fullMask = 1<<len(nums)
        def backtrack(cand,cur):
            if len(cur) == len(nums):
                res.append(cur[::])
                return
                
            for i in range(len(cand)): 
                
                cur.append(cand[i])
                
                next_option = cand[:i] + cand[i+1:]
                backtrack(next_option, cur)
                
                cur.pop()
            
        backtrack(nums,[])
        return res