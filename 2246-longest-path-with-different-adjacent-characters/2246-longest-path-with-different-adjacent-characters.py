class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        graph = defaultdict(list)
        for i in range(1,len(parent)):
            graph[parent[i]].append(i)
            
        ans = 1
        def dfs(node):
            nonlocal ans
            if  not graph[node]:
                return s[node]
            
            temp = []
            
            for neighbour in graph[node]:
                returned = dfs(neighbour)
                
                if s[node] != returned[-1]:
                    if len(temp) < 2:
                        temp.append(returned)
                        
                    elif len(temp) == 2:
                        if len(returned)>len(temp[0]):
                            temp[0] = returned
                            
                    temp = sorted(temp,key = lambda x:len(x))
                    
            if not temp:
                return s[node]
            if len(temp) == 1:
                ans = max(ans,len(temp[0])+1)
                return temp[0]+s[node]
            
            ans = max(ans,len(temp[-1])+len(temp[-2])+1)
            
            return temp[-1]+s[node]
        dfs(0)
        return ans