class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        
        def heleper(l,r,turn):
            if l > r :
                return 0
            
            if turn:
                return max(nums[l] + heleper(l+1, r, not turn),  nums[r] + heleper(l, r-1, not turn))
            
            else:
                return min(-nums[l] + heleper(l+1, r, not turn),-nums[r] + heleper(l, r-1, not turn))
        
        return heleper(0,len(nums)-1,True) >= 0
            
                