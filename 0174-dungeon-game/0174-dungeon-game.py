class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        for i in range(len(dungeon)-1,-1,-1):
            for j in range(len(dungeon[0])-1,-1,-1):
                if i+1 == len(dungeon) and j + 1 == len(dungeon[0]):
                    dungeon[i][j] = min(0, dungeon[i][j])

                elif i+1 == len(dungeon) and j + 1 < len(dungeon[0]):
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i][j+1])
                
                elif i+1 < len(dungeon) and j+1 == len(dungeon[0]):
                    dungeon[i][j] = min(0, dungeon[i][j] + dungeon[i+1][j])
                else:
                    dungeon[i][j] = min(0, dungeon[i][j] + max(dungeon[i+1][j], dungeon[i][j+1]))
        
        return abs(dungeon[0][0]) + 1
        