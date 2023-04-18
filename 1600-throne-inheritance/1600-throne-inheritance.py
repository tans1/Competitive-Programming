class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.deleted = defaultdict(bool)
        self.kingname = kingName
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)

    def death(self, name: str) -> None:
        self.deleted[name] = True

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node,ans,visited):
            visited.add(node)
            if self.deleted[node] == False:
                ans.append(node)

            for nb in self.graph[node]:
                if nb not in visited:
                    dfs(nb,ans,visited)

            return ans
        nd = self.kingname
        return dfs(nd, [], set())
    
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()