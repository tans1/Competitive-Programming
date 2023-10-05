class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if (jug1Capacity + jug2Capacity) < targetCapacity:
            return False
            
        visited = set()
        temp = 0
        while temp not in visited:
            visited.add(temp)
            if temp == targetCapacity:
                return True
            if temp < targetCapacity:
                temp += max(jug1Capacity,jug2Capacity)
            else:
                temp -= min(jug1Capacity,jug2Capacity)

        return False
            