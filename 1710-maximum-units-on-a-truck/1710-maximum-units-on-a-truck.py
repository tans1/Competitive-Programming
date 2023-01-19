class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes = sorted(boxTypes, key= lambda x: -x[1])

        res = 0
        i = 0
        while i < len(boxes) and truckSize > 0:
            if boxes[i][0] <= truckSize:
                res += boxes[i][0] * boxes[i][1]
                truckSize -= boxes[i][0]
            
            else:
                res += truckSize * boxes[i][1]
                
                truckSize = 0
            i += 1
        
        return res