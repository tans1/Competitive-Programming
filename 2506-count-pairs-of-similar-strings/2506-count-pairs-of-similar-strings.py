class Solution:
    def similarPairs(self, words: List[str]) -> int:
        dic = defaultdict(int)
        for word in words:
            a = list(dict(Counter(word)).keys())
            a.sort()
            unique = ''.join(a)
            dic[unique] += 1
            
        temp = []
        for i in dic.values():
            if i > 1: temp.append(i)
        res = 0
        for i in temp:
            b = math.perm(i)
            c = (math.perm(i-2)) * 2
            res += b // c
        return res
