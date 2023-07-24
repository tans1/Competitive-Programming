class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0] * (i+1) for i in range(101)]
        dp[0][0] = poured
        for r in range(query_row + 1):
            for c in range(r+1):
                if dp[r][c] > 1:
                    dp[r+1][c] += (dp[r][c] - 1) / 2
                    dp[r+1][c+1] += (dp[r][c] - 1) / 2

        return min(1, dp[query_row][query_glass])