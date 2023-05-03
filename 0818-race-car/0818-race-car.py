class Solution:
    def racecar(self, target: int) -> int:
        q = deque()
        q.append((0,1,0))

        while q:
            pos, speed, steps = q.popleft()
            
            # accelate
            if pos  == target:
                return steps
            
            
            
            q.append((pos + speed, speed * 2, steps + 1))
            

            # reverse
            if (speed > 0 and pos + speed > target) or (speed < 0 and pos + speed < target):
                if speed > 0:
                    q.append((pos, -1, steps + 1))
                else:
                    q.append((pos, 1, steps + 1))
    
                


