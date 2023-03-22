class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)
        temp = set()
        
        
        def dfs(cur, i):
            if len(cur) > 1:
                temp.add(tuple(cur))
                
            if i >= n:
                if len(cur) > 1:
                    temp.add(tuple(cur))
                return

            
            if len(cur) > 0:
                if nums[i] >= cur[-1]:
                    cur.append(nums[i])
                    dfs(cur, i +1)

                    cur.pop()
                dfs(cur, i + 1)
                    
                
            else:
                cur.append(nums[i])
                dfs(cur, i +1)
                
                cur.pop()
                dfs(cur, i + 1)
        
        
        dfs([],0)
        res = list(map(list, temp))
        return res
        