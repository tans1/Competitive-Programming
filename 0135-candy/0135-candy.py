class Solution:
    def candy(self, ratings: List[int]) -> int:
        temp1 = [1 for _ in range(len(ratings))]
        temp2 = [1 for _ in range(len(ratings))]
        
        for i in range(1,len(ratings)):
            if ratings[i] > ratings[i-1]:
                temp1[i] = temp1[i-1] + 1
        for j in range(len(ratings)-2,-1,-1):
            if ratings[j] > ratings[j+1]:
                temp2[j] = temp2[j+1] + 1
        
        ans = 0
        for i in range(len(ratings)):
            ans += max(temp1[i],temp2[i])
        return ans
        