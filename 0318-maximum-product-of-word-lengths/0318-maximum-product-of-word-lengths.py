class Solution:
    def maxProduct(self, words: List[str]) -> int:
        temp = []
        for word in words:
            mask = 0
            for w in word:
                mask |= 1 <<(ord(w) - ord('a'))
            temp.append(mask)
        
        ans = 0
        for i in range(len(temp)-1):
            for j in range(i+1,len(temp)):
                if not (temp[i] & temp[j]):
                    ln = len(words[i]) * len(words[j])
                    ans = max(ans, ln)
        return ans