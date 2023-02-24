class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        fr = Counter(s)
        
        st = []
        
        for i,v in enumerate(s):
            while st and st[-1] > v and fr[st[-1]] > 0:
                if v not in st:
                    st.pop()
                else:
                    break
            if v not in st:    
                st.append(v)
            fr[v] -= 1
        return ''.join(st)