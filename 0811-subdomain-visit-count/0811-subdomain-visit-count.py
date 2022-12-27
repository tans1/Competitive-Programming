class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = defaultdict(int)
        res = []
        for domain in cpdomains:
            dmn = domain.replace(' ','.')
            ds = dmn.split('.')
            i = len(ds)-1
            while i > 0:
                dic['.'.join(ds[i:])] += int(ds[0])
                i -= 1
        res = []
        for key, value in dic.items():
            temp = str(value) + ' ' + key
            res.append(temp)
        return res
            
            
        