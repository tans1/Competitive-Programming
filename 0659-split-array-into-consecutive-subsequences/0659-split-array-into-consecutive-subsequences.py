class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        frequncy = Counter(nums)
        needed = defaultdict(int)
        
        for n in nums:
            if frequncy[n] == 0:
                continue
            
            if needed[n] > 0:
                needed[n] -= 1
                needed[n+1] += 1
                
            
            elif frequncy[n+1] > 0 and frequncy[n + 2] > 0:
                frequncy[n+1] -= 1
                frequncy[n+2] -= 1
                needed[n+3] += 1
            
            elif needed[n] == 0 or frequncy[n+1] <= 0 or frequncy[n+2] <= 0:
                return False
            
            frequncy[n] -= 1
        return True
                
