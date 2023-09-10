class Solution:
    def countOrders(self, n: int) -> int:
        slots = 2 * n
        ans = 1
        while slots > 0:
            valid = slots * (slots - 1) // 2
            ans *= valid
            slots -= 2
        return ans % (10**9 + 7)