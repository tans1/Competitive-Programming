class Solution:
    def arrangeWords(self, text: str) -> str:
        temp_List = text.split(" ")
        temp2 = sorted(temp_List, key = lambda x:(len(x)))
        
        res = " ".join(temp2).capitalize()

        return res