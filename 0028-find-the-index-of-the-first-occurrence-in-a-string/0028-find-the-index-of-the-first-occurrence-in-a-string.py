class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j < len(haystack) and haystack[i+j] != needle[j]:
                    break
            if i+j < len(haystack)  and haystack[i+j] == needle[j] and j + 1 == len(needle):
                return i
        return -1