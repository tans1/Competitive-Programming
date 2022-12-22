class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = set()
        loosers = set()
        freq = defaultdict(int)
        lost_only_once = []
        
        for match in matches:
            winners.add(match[0])
            loosers.add(match[1])
            freq[match[1]] += 1
            
        for key, value in freq.items():
            if value == 1:
                lost_only_once.append(key)
                
        winners = sorted(winners - loosers)
        lost_only_once.sort()
        
        return [winners, lost_only_once]
        