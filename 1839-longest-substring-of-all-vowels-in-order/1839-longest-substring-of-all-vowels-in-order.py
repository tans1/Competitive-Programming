class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        if (len(word) < 5) or len(Counter(word)) < 5:
            return 0
        i = 0
        j = 1
        temp = set(word[i])
        ans = 0

        while i <= j and j < len(word):
            if word[j] >= word[j-1]:
                temp.add(word[j])
            else:
                if len(temp) == 5:
                    ans = max(ans, j - i)
                temp.clear()
                i = j
                temp.add(word[i])
            j += 1
            
        if len(temp) == 5:
            ans = max(ans, j - i)
        return ans

