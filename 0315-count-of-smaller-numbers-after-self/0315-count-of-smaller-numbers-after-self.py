class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums.reverse()
        srt = []
        ans = []
        
        for n in nums:
            i = bisect_left(srt, n)
            ans.append(i)
            srt.insert(i, n)
        ans.reverse()
        return ans
            