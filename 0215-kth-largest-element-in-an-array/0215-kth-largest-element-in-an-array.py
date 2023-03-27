class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        mx , mn = max(nums) , min(nums)
        srt = []
        
        if mn >= 0:
            temp = [0 for i in range(max(mx, len(nums))+1)]
            for n in nums:
                temp[n] += 1
            for i in range(len(temp)):
                if temp[i] > 0:
                    srt.extend([i for j in range(temp[i])])
        else:
            if mx >= 0:
                temp = [0 for i in range(mx - mn + 1)]
            else:
                temp = [0 for i in range(max(abs(mn), len(nums))+1)]
            for n in nums:
                temp[n-mn] += 1
            for i in range(len(temp)):
                if temp[i] > 0:
                    srt.extend([(i+mn) for j in range(temp[i])])
            
        return srt[-k]