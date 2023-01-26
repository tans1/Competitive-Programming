class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        cnt = 0
        
        i = 0
        j = len(nums)-1
        
        while i < j:
            if nums[i] + nums[j] == k:
                cnt += 1
                i += 1
                j -= 1
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
                
        return cnt
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cnt = 0
#         dic = defaultdict(int)
#         for n in nums:
#             if k - n in dic and dic[k-n] > 0:
#                 cnt += 1
#                 dic[k-n] -= 1
#             else:
#                 dic[n] += 1
#         return cnt
#         counter = 0
#         temporaryDIC = {}
#         for i in nums:
#             j = k -i
#             if j in temporaryDIC and temporaryDIC[j] >0:
#                 counter +=1
#                 temporaryDIC[j] -=1
#             else:
#                 if i not in temporaryDIC:
#                     temporaryDIC[i] = 0
#                 temporaryDIC[i] +=1
#         return counter
                    