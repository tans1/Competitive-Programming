class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        temp = set()
        n = len(nums)
        nums.sort()
        
        def backtracking(cur, i):
            if i >= n:
                temp.add(tuple(cur))
                return
            
            cur.append(nums[i])
            backtracking(cur, i +1)
            
            cur.pop()
            backtracking(cur, i +1)
        
        backtracking([], 0)
        
        res = list(map(list , temp))
        return res