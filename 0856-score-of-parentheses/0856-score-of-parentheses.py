class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if len(s) == 2: return 1
        st = []
        res = 0
        mx = 0
        for i in range(len(s)):
            if s[i] == '(':
                st.append('(')
                res += mx
                mx = 0
            else:
                st.pop()
                if st:
                    mx = max(mx, 2 **(len(st)))
                else:
                    mx = max(mx,1)
        res += mx
        return res
    