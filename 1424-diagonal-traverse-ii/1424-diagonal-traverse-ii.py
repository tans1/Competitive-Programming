class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        dic = defaultdict(list)
        row = len(nums)
        for i in range(row):
            for j in range(len(nums[i])):
                dic[i+j].append(nums[i][j])
        res = []
        for key, values in dic.items():
            values.reverse()
            res += values
        return res
#         temp = list(dic.values())

#         i = 0
#         while i < len(temp):
#             temp[i].reverse()
#             i += 1
#         res = temp[0]
#         for i in range(1,len(temp)):
#             res.extend(temp[i])
#         return res