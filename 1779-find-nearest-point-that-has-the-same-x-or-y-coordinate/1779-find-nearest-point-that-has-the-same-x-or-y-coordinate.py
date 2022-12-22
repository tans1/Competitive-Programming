class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        dic = {}
        res = []
        
        for index in range(len(points)):
            if points[index][0] == x or points[index][1] == y: #f it is valid
                md = abs(x - points[index][0]) + abs(y - points[index][1])
                dic[index] = md
                
        if len(dic) != 0:  #if there is any valid value in the points
            sorted_dic = sorted(dic.items(), key = lambda x:(x[1],x[0]))
            minn = sorted_dic[0][1]
            
            for i in range(len(sorted_dic)):
                if sorted_dic[i][1] == minn :
                    res.append(sorted_dic[i][0])
            return res[0]
        else:   #if there is no any valid value in the points
            return -1
            
                    
        