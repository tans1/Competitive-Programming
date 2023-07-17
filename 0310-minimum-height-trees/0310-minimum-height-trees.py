class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        degree = defaultdict(int)
        tree = defaultdict(list)
        for u,v in edges:
            degree[u] += 1
            degree[v] += 1
            
            tree[u].append(v)
            tree[v].append(u)
        
        
        q = []
        for k,v in degree.items():
            if v == 1:
                q.append(k)

        
        visited = set()
        while q :
            new_q = []
            for cur_node in q:
                visited.add(cur_node)
                for nb in tree[cur_node]:
                    if nb not in visited:
                        degree[nb] -= 1
                        

                        if degree[nb] == 1:
                            new_q.append(nb)

            if len(new_q) > 0:
                q = new_q
            else:
                break
        if q:
            return q
        else:
            return [0]
        
        