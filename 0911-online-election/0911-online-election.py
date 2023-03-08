class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.dct = defaultdict(int) # to track who is winiing at each given tine
        
        for i in range(len(persons)):
            frq = Counter(persons[:i+1])
            srt = sorted(frq.items(), key =lambda x:-x[1])
            
            if len(srt) > 1 and srt[0][1] == srt[1][1]: # if there is tie
                tr = srt[0][1]
                j = i
                while j > -1 and frq[persons[j]] < tr:
                    j -= 1
                
                if frq[persons[j]] == tr:
                    self.dct[times[i]] = persons[j]
            else:
                self.dct[times[i]] = srt[0][0]
                
    def q(self, t: int) -> int:
        val = list(self.dct.keys())
        i = bisect_left(val,t)
        if i < len(val) and val[i] == t:
            return self.dct[val[i]]
        else:
            return self.dct[val[i-1]]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)