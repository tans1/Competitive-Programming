class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        tempdic = defaultdict(int)
        cnt = 0
        sm = 0
        for n in nums:
            sm += n
            if sm == goal:
                cnt += 1
            if sm - goal in tempdic:
                cnt += tempdic[sm-goal]
            tempdic[sm] += 1
            
        return cnt

            
                
                
            
                
            