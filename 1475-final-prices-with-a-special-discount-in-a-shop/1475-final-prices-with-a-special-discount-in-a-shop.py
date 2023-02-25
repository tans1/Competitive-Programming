class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        mn = [0] * len(prices)
        st = []
        for i, v in enumerate(prices):
            while st and v <= st[-1][0]:
                n , j = st.pop()
                mn[j] = v
            st.append([v,i])
        
        for i in range(len(prices)):
            prices[i] -= mn[i]
        return prices