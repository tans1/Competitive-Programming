class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        temp =  defaultdict(int)
        for i in range(len(heaters)):
            temp[heaters[i]] = 0
        for j in range(len(houses)):
            if houses[j] not in temp:
                temp[houses[j]] = float("inf")
        temp2 = list(map(list, temp.items()))
        temp2.sort()
        
        for i in range(len(temp2)):
            l , r = i , i
            if temp2[i][-1] == float("inf"):
                while l >= 0 and temp2[l][-1] == float("inf"):
                    l -= 1
                while r < len(temp2) and temp2[r][-1] == float("inf"):
                    r += 1
                    
                left = float("inf")
                if l >= 0 and temp2[l][-1] != float("inf"):
                    left = abs(temp2[i][0] - temp2[l][0] + temp2[l][-1])
                    
                right = float("inf")
                if r < len(temp2) and temp2[r][-1] != float("inf"):
                    right = abs(temp2[r][0] - temp2[i][0])
                    
                
                temp2[i][-1] = min(left,right)
        ans = sorted(temp2, key = lambda x : x[1])
        return ans[-1][-1]
        