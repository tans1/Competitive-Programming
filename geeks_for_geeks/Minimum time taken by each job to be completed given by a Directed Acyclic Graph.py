from typing import List
from collections import *

class Solution:
  def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
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
            
