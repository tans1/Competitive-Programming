class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends=[i for i in range(1,n+1)]
        i = k-1
        
        while len(friends) > 1:
            friends.pop(i)
            
            i += (k-1)
            i = i%len(friends)
        return friends[0]