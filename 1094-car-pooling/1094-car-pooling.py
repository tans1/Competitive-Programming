class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        begin = sorted(trips, key = lambda x: x[1]) #sort by where peoples are picked up 
        end =  sorted(trips, key = lambda x: -x[2]) #sort by where the are droped
        
        path = [0] * (end[0][2] + 1)
        
        for trip in trips:  # draw coordinate axis
            path[trip[1]] += trip[0]
            path[trip[2]] -= trip[0]
        
        i = 0
        while i < len(path) and capacity >= 0:
            capacity -= path[i]
            i += 1
        return capacity >= 0
        