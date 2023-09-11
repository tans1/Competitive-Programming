class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        dct = {i : groupSizes[i] for i in range(len(groupSizes))}
        sortedGroup = sorted(dct.items(), key = lambda x: x[1])
        
        ans = []
        curGroup = []
        
        for Id, size in sortedGroup:
            if len(curGroup) + 1 <= size:
                curGroup.append(Id)
            
            if len(curGroup) == size:
                ans.append(curGroup)
                curGroup = []
                
        return ans