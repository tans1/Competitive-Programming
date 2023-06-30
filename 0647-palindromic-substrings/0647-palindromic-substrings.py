class Solution:
    def countSubstrings(self, s: str) -> int:
        def checkPalindrome(string):
            i = 0
            j = len(string) - 1
            while i <= j:
                if string[i] != string[j]:
                    return False
                i += 1
                j -= 1
            return True
        
        ans = 0
        for i in range(len(s)):
            for j in range(i,len(s)):
                ans += checkPalindrome(s[i:j+1])
        
        return ans