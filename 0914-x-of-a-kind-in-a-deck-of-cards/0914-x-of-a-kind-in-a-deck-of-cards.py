class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        temp = list(Counter(deck).values())
        return math.gcd(*temp) >= 2