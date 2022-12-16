class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i].isalnum():
                st.append(s[i].lower())
        i = 0
        j = len(st)-1
        while i <= j:
            if st[i] != st[j]:
                return False
            i +=1
            j -= 1
        return True