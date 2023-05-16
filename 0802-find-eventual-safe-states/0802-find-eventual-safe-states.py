class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        grp = {}
        terminal = set()
        for i in range(len(graph)):
            grp[i] = graph[i]
            if not len(graph[i]):
                terminal.add(i)
        
        color = [-1 for _ in range(len(graph))]
        opt = {}
        
        def dfs(nd):
            if nd in terminal :
                opt[nd] = True
                color[nd] = 1
                return True

            for nb in grp[nd]:
                if color[nb] == 0:
                    opt[nd] = False
                    return False

                elif nb in opt and opt[nb] == False:
                    opt[nd] = False
                    return False
                
                elif nb not in opt:
                    color[nb] = 0
                    if not dfs(nb):
                        opt[nd] = False
                        return False
            
            color[nd] = 1
            opt[nd] = True
            return True
        for i in range(len(graph)):
            if i not in opt:
                dfs(i)
            
        ans = []
        ans = [k for k,v in opt.items() if v == True]
        ans.sort()
        return ans
            
                
                
                