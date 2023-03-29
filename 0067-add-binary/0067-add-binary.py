class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == "0" and b == "0":
            return "0"
        nm1 = int(a,2)
        nm2 = int(b,2)
        c = bin(nm1 + nm2)
        return c.lstrip('0b')