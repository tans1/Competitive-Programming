class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        dct = {
            "a" : 1,
            "b" : 2,
            "c" : 3,
            "d" : 4,
            "e" : 5,
            "f" : 6,
            "g" : 7,
            "h" : 8
        }
        
        x , y = coordinates[0], coordinates[1]
        
        return (dct[x] + int(y)) % 2 != 0