class Solution:
    def reverseWords(self, s: str) -> str:
        def reversee(word):
            temp = list(word)
            temp.reverse()
            return ''.join(temp)
            
        return " ".join(list(map(reversee, s.split())))
        