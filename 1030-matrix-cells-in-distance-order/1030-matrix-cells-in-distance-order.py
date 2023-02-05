class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        dct = defaultdict(list)
        
        for i in range(rows):
            for j in range(cols):
                distance = abs(i-rCenter) + abs(j-cCenter)
                dct[distance].append([i,j])
        dct = sorted(dct.items(), key=lambda x:x[0])
        res = []
        for r in dct:
            res += r[1]
        return res
