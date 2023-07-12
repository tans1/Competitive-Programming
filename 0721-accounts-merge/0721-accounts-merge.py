class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            par1, par2 = find(x), find(y)
            parent[par1] = par2
        
        temp1 = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                temp1[email].append(i)
        
        for indices in temp1.values():
            for i in indices[1:]:
                union(indices[0], i)
        
        temp2 = defaultdict(set)
        for i, account in enumerate(accounts):
            temp2[find(i)].update(account[1:])
        
        ans = []
        for i, emails in temp2.items():
            ans.append([accounts[i][0]] + sorted(emails) )
        return ans