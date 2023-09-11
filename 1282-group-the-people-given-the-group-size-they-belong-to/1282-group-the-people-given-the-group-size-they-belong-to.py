class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dct = {i : groupSizes[i] for i in range(len(groupSizes))}
        sortedGroup = sorted(dct.items(), key = lambda x: x[1])
        
        ans = []
        temp = []
        
        for Id, size in sortedGroup:
            if len(temp) + 1 <= size:
                temp.append(Id)
            
            if len(temp) == size:
                ans.append(temp)
                temp = []
                
        return ans