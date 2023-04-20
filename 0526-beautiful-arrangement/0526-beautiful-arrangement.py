class Solution:
    def countArrangement(self, n: int) -> int:
        nums = [i for i in range(1,n+1)]
        
        perm = []
        def backtrack(cand,cur, ln):
            if ln == len(nums):
                perm.append(cur[::])
                return
                
            for i in range(len(cand)):
                if cand[i] % (ln+1) == 0 or (ln+1) % cand[i] == 0:
                    
                    cur.append(cand[i])
                    next_option = cand[:i] + cand[i+1:]
                    backtrack(next_option, cur,ln+1)

                    cur.pop()
        backtrack(nums,[],0)
        return len(perm)
        