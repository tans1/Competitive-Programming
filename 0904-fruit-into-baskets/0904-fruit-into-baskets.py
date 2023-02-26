class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        res = 0
        i = 0
        seen = defaultdict(int)
        for j in range(len(fruits)):
            seen[fruits[j]] += 1
            
            while len(seen) > 2 and i < j:
                seen[fruits[i]] -= 1
                
                if seen[fruits[i]] == 0:
                    del seen[fruits[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
                