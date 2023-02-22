class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        # a b c a b c b b
        # set = ( a, b, c, a   )
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in st:
                st.add(s[r])
            else:
                res = max(res,r-l)
                while s[l] != s[r]:
                    if s[l] in st:
                        st.remove(s[l])
                    l += 1
                
                l+=1
            res = max(res,r-l+1)
        return res
