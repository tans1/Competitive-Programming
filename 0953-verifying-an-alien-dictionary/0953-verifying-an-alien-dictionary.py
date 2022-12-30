class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dct = {order[i]:i+1 for i in range(len(order))}
        j = 0
        while j < len(words)-1:
            crt = words[j]
            nxt = words[j+1]
            flag = True
            for i in range(min(len(crt), len(nxt))):
                flag = False
                if dct[crt[i]] > dct[nxt[i]]:
                    return False
                elif dct[crt[i]] < dct[nxt[i]]:
                    flag = True
                    break
            if not flag and len(crt) > len(nxt):
                return False
            j += 1
        return True
            
            
        
    