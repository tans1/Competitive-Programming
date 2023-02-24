class Solution:
    def minOperations(self, logs: List[str]) -> int:
        path = []
        # temp = 0
        for p in logs:
            if p not in ['./','../']:
                path.append(p)
                #temp += 1
            elif p == '../':
                if path:
                    path.pop()
                    #temp -= 1
        
        return len(path) #temp