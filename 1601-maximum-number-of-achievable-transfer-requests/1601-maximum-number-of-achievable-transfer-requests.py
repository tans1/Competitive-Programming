class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        r = len(requests)
        ans = 0
        movement = defaultdict(int)
        
        def backtracking(i, count):
            nonlocal ans
            if i == r:
                for k ,v in movement.items():
                    if v != 0:
                        return
                ans = max(ans, count)
                return
            frm = requests[i][0]
            to = requests[i][1]
            
            movement[frm] -= 1
            movement[to]  += 1
            backtracking(i+1, count+1)
            
            
            movement[frm] += 1
            movement[to]  -= 1
            backtracking(i+1, count)
        backtracking(0,0)
        return ans