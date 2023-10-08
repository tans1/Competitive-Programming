class Solution:
    def knightDialer(self, n: int) -> int:
        # Buttom Up
        mod = 10 ** 9 + 7
#         moves = {
#             0 : [4,6],
#             1 : [6,8],
#             2 : [7,9],
#             3 : [4,8],
#             4 : [0,3,9],
#             5 : [],
#             6 : [1,7,0],
#             7 : [2,6],
#             8 : [1,3],
#             9 : [4,2]
#         }
#         ways_toReach = [1 for _ in range(10)]
#         for _ in range(n-1):
#             next_ = [0 for _ in range(10)]
#             for num in range(10):
#                 for option in moves[num]:
#                     next_[num] += ways_toReach[option]
#             ways_toReach = next_
#         return sum(ways_toReach) % mod
        
        
        
        
        
        # Top Down
        memo = {}
        directions = [(-2,-1),(-2,1),(-1,-2),(-1,2),(1,2),(1,-2),(2,1),(2,-1)]
        
        def dfs(i,j,n_):
            if n_ == 1:
                return 1
            
            if (i,j,n_) in memo:
                return memo[(i,j,n_)]
            
            memo[(i,j,n_)] = 0
            for l,k in directions:
                
                if 0 <= i+l < 4 and 0 <= j+k < 3 and (i+l,j+k) not in [(3,0),(3,2)]:
                    memo[(i,j,n_)] += dfs(i+l , j+k , n_ - 1)
            return memo[(i,j,n_)]
        
        ans = 0
        for i in range(4):
            for j in range(3):
                if (i, j ) not in [(3,0),(3,2)]:
                    ans += dfs(i,j,n)
        return ans % mod