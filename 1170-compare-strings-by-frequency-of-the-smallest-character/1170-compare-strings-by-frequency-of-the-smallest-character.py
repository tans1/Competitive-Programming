class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        fw = []
        for i in range(len(words)):
            tmp = list(words[i])
            tmp.sort()
            fw.append(tmp.count(tmp[0]))
        
        fw.sort()
        ans = []
        n = len(fw)
        
        for qr in queries:
            tmp = list(qr)
            tmp.sort()
            f = tmp.count(tmp[0])

            i = n - 1
            cnt = 0
            while i > -1 and fw[i] > f:
                cnt += 1
                i -= 1
            ans.append(cnt)
        
        return ans


