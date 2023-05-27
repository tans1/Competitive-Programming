class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequncy = Counter(nums)
        can_join = defaultdict(int)
        
        for n in nums:
            if frequncy[n] == 0:
                continue
            
            if can_join[n] > 0:
                can_join[n] -= 1
                can_join[n+1] += 1
                
            
            elif frequncy[n+1] > 0 and frequncy[n + 2] > 0:
                frequncy[n+1] -= 1
                frequncy[n+2] -= 1
                can_join[n+3] += 1
            
            elif can_join[n] == 0 or frequncy[n+1] <= 0 or frequncy[n+2] <= 0:
                return False
            
            frequncy[n] -= 1
        return True
                
