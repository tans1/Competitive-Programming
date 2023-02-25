class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        res = 0
        l = 0
        for r in range(len(s)):
            if s[r] not in st:
                st.add(s[r])
            else:
                # res = max(res,r-l)
                while s[l] != s[r]:
                    st.remove(s[l])
                    l += 1
                
                l+=1
            res = max(res,r-l+1)
        return res
