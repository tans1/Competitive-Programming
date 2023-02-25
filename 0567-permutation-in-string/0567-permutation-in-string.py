class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        temp1 = Counter(s1)
        i, j = 0, len(s1)
        while j <= len(s2):
            window = s2[i:j]
            temp2 = Counter(window)
            if  temp2 == temp1:
                return True
            i += 1
            j += 1
        return False