class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        temp2 = []
        for n in arr:
            temp2.append([n,bin(n)])
        temp = sorted(temp2, key=lambda x: (x[1].count('1'), x[0]))
        print(temp)
        res = []
        for n in temp:
            res.append(n[0])
        return res