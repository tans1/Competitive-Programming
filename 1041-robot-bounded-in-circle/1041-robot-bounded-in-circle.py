class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = {
            "N":{ "L" : "W", "R" : "E" },
            "S":{ "L" : "E", "R" : "W" },
            "W":{ "L" : "S", "R" : "N" },
            "E":{ "L" : "N", "R" : "S" }
        }
        
        curr = [0,0,"N"]
        visited = set()
        visited.add((0,0))
        prev = (0,0)
        for i in range(len(instructions)):
            if instructions[i] == "G":
                if curr[-1] == "N": curr[1] += 1
                elif curr[-1] == "W": curr[0] -= 1
                elif curr[-1] == "E": curr[0] += 1
                else: curr[1] -= 1
            else:
                curr[-1] = directions[curr[-1]][instructions[i]]

        if curr[0] == curr[1] == 0 or curr[-1] != "N":
            return True
        return False
