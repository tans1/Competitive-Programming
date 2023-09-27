class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        count = 0
        letter = ''
        for i in range(len(s)):
            if s[i].isdigit():
                count *= int(s[i])
            else:
                count += 1
                letter = s[i]

            if count > k:
                break
            
            if count == k:
                return letter
            
        for j in range(i, -1, -1):
            if s[j].isdigit():
                count /= int(s[j])
            else:
                if k > count:
                    k %= count
                if k == 0 or count == k:
                    return s[j]
                count -= 1    