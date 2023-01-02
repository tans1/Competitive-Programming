class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True
        elif len(word) == 2:
            if ord(word[0]) not in range(65,91) and ord(word[1]) in range(65,91):
                return False
            else:
                return True
        else:

            if ord(word[0]) in range(65,91):
                if ord(word[1]) in range(65,91):
                    for i in range(2,len(word)):
                        if ord(word[i]) not in range(65,91):
                            return False
                else:
                    for i in range(2,len(word)):
                        if ord(word[i]) in range(65,91):
                            return False
            else:
                for i in range(1,len(word)):
                    if ord(word[i]) in range(65,91):
                        return False


            return True