class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        dic = defaultdict(list)
        
        for path in paths:
            temp = path.split(' ')
            directory = temp[0]
            
            for file in temp[1:]:
                temp2 = file.split('(')
                dic[temp2[1][:-1]].append(directory + '/' + temp2[0])
        res = []
        for key, value in dic.items():
            if len(value) > 1 : res.append(value)
        return res