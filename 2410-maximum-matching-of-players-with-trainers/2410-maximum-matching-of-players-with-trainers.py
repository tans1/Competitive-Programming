class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        cnt = 0
        
        i = 0
        j = 0
        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                cnt  += 1
                i += 1
                j += 1
            else:
                j += 1
        return cnt
        