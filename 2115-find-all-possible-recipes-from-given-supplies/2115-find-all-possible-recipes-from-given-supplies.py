class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incoming = defaultdict(int)
        
        for i in range(len(recipes)):
            for nb in ingredients[i]:
                graph[nb].append(recipes[i])
            incoming[recipes[i]] += len(ingredients[i])
        q = deque(supplies)
        
        ans = []
        while q:
            nd = q.popleft()
            if nd in recipes:
                ans.append(nd)
            
            for nb in graph[nd]:
                incoming[nb] -= 1
                
                if incoming[nb] == 0:
                    q.append(nb)
        return ans