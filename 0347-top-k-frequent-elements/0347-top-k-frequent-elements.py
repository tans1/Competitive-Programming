class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for num in nums:
            if num in dic: dic[num] += 1
            else:
                dic[num] = 1
        temp1 = []
        for v in dic.items():
            temp1.append(list(v))
        temp1.sort(key=lambda x:x[1])
        temp1 = temp1[::-1]
        res = []
        i = 0
        while i < k:
            res.append(temp1[i][0])
            i += 1
        return res