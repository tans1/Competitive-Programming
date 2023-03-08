class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        
        def helper(n,k):
            if n == 1:
                return 0
            
            if k % 2 == 0:
                up = helper(n-1,k // 2)
            else:
                up = helper(n-1,(k // 2) + 1)
                
            if k % 2 == 0:
                res = 0 if up == 1 else 1
            else:
                res = up
            return res
        
        return helper(n,k)
            
            
        
#         def helper(n):
#             if n == 1:
#                 return "0"
            
#             up = helper(n-1)
#             res = ""
#             for i in range(len(up)):
#                 if up[i] == "0":
#                     res += "01"
#                 else:
#                     res += "10"
#             return res
        
#         ans = helper(n)
#         return int(ans[k-1])