class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = [-1 for _ in range(len(s))]
        def find(u):
            root = u
            while root != parent[root] and parent[root] != -1:
                root = parent[root]
            while u != root:
                ancestor = parent[u]
                parent[u] = root
                u = ancestor
            return root
        def union(u,v):
            rt1 = find(u)
            rt2 = find(v)
            if rt1 < rt2:
                parent[rt2] = rt1
            else:
                parent[rt1] = rt2
        
        for u,v in pairs:
            union(u,v)
        dct = defaultdict(list)
        for i in range(len(s)):
            dct[find(i)].append(i)
        temp = [0 for _ in range(len(s))]
        for i  in range(len(s)):
            temp2 = dct[i]
            temp3 = [s[j] for j in temp2]
            temp2.sort()
            temp3.sort()
            for j in range(len(temp2)):
                temp[temp2[j]] = temp3[j]
        return ''.join(temp)
                
        