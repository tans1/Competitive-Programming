class Solution:
    def numTeams(self, rating: List[int]) -> int:
        less_ = [0 for _ in range(len(rating))]
        more_ = [0 for _ in range(len(rating))]
        
        ans = 0
        for i in range(len(rating)):
            for j in range(i):
                if rating[j] < rating[i]:
                    ans += less_[j]
                    less_[i] += 1
                elif rating[j] > rating[i]:
                    ans += more_[j]
                    more_[i] += 1
        return ans