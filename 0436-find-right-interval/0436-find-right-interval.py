class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        for i in range(n):
            intervals[i].append(i)
        
        res = []
        intervals = sorted(intervals, key=lambda x: x[0])

        for i in range(n):
            target = intervals[i][1]
            l , r = 0 , n-1
            ap = float('inf')
            while l <= r:
                md = (l + r) // 2
                if target <= intervals[md][0]:
                    ap = min(ap,intervals[md][2])
                    r = md - 1

                else:
                    l = md + 1
            
            if ap == float('inf'):
                res.append([-1, intervals[i][2]])
            else:
                res.append([ap, intervals[i][2]])

        temp = sorted(res, key = lambda x: x[1])
        ans = []
        for x in temp:
            ans.append(x[0])

        return ans

