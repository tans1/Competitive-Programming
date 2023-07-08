class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        parent = [-1 for _ in range(len(source))]
        def find(x):
            root = x
            while root != parent[root] and parent[root] != -1:
                root = parent[root]
            while x != root:
                ancestor = parent[x]
                parent[x] = root
                x = ancestor
            return root
        def union(l,m):
            root1 = find(l)
            root2 = find(m)
            parent[root2] = root1
        
        for i,j in allowedSwaps:
            union(i,j)
        
        # root : childs
        temp = defaultdict(list)
        for  i in range(len(source)):
            temp[find(i)].append(i)
        
        ham_dis = 0
        temp2 = list(temp.values()) # same groups
        for index in temp2:
            tempSource = []
            tempTarget = []
            for i in index:
                tempSource.append(source[i])
                tempTarget.append(target[i])
            sourceFreq = Counter(tempSource)
            targetFreq = Counter(tempTarget )
            ham_dis += (sum((sourceFreq-targetFreq).values()) + sum((targetFreq-sourceFreq).values()) ) // 2
        return ham_dis