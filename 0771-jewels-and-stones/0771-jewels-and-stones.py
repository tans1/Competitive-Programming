class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        temp = Counter(stones)
        st1 = set(list(jewels))
        st2 = set(list(temp.keys()))
        
        tem2 = st2.intersection(st1)
        
        ans = 0
        for l in tem2:
            ans += temp[l]
        
        return ans