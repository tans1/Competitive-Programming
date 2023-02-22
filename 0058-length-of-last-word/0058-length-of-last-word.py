class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        temp = s.split()
        return len(temp[-1])