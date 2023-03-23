class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        ans = []
        def dfs(cur, destination, path):
            if cur == destination:
                ans.append(path[:])
                return
            if not path:
                path.append(cur)
            for nd in graph[cur]:
                path.append(nd)
                dfs(nd, destination,path)

                path.pop()
        dfs(0, len(graph)-1, [])
        return ans