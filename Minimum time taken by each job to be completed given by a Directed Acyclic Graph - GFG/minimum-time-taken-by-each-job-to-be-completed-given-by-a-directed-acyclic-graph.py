from typing import List
from collections import *

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here

        indegree = [0 for _ in range(n+1)]
        ans = [0 for _ in range(n+1)]
        
        graph = defaultdict(list)
        
        
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            
            graph[u].append(v)
            indegree[v] += 1
            
        q = deque([])
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        while q:
            cur_node = q.popleft()
            ans[cur_node] += 1
            
            for nb in graph[cur_node]:
                indegree[nb] -= 1
                ans[nb] = max(ans[nb], ans[cur_node])
                
                if indegree[nb] == 0:
                    q.append(nb)
                    
        return ans[1:]
            
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends