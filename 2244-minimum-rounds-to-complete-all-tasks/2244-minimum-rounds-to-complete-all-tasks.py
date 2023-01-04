class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ts = Counter(tasks)
        res = 0
        for k, v in ts.items():
            if v < 2:
                return -1
            else:
                res += math.ceil(v / 3)
        return res
            