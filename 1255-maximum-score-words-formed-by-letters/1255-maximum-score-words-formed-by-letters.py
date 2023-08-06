class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        frequency = Counter(letters)
        scr = { chr(i+97) : v  for i,v in enumerate(score) if v > 0 }
        
        def dfs(i,frq,scor):
            if i >= len(words):
                return scor
            
            cur = 0
            word = words[i]
            newFreq = frq.copy()

            for j,v in enumerate(word):
                if v not in newFreq or newFreq[v] <= 0:
                    cur = 0
                    break
                else:
                    cur += scr[v]
                    newFreq[v] -= 1
            
            return max(dfs(i+1, newFreq , cur + scor), dfs(i+1,frq, scor))
        
        return dfs(0,frequency,0)
        