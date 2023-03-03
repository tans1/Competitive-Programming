class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0
        while tickets[k] > 1:
            t = tickets.pop(0)
            if t > 1:
                tickets.append(t-1)
                
            if k == 0:
                k = len(tickets) -1
            else:
                k -= 1
            cnt += 1
        return cnt + k + 1