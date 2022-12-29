class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        res = []
        es = sum(filter(lambda x: x%2 == 0,nums)) #sum of even numbers in nums
        for q in queries:
            pointer1 = nums[q[1]]
            nums[q[1]] = nums[q[1]] + q[0]
            
            if pointer1 % 2 == 0:
                es -= pointer1
            if nums[q[1]] % 2 == 0:
                es += nums[q[1]]
                res.append(es)
                
            else:
                res.append(es)
                
        return res
            
            