class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lsp = [0 for _ in range(len(b))]
        i , j = 0 , 1
        while j < len(b):
            if b[i] == b[j]:
                lsp[j] = i+1
                i  = i+1
                j = j + 1
            else:
                if i == 0:
                    j += 1
                else:
                    i = lsp[i-1]
        
        i , j = 0 , 0
        temp =  0
        visited = set()
        while i < len(a) or ( i >= len(a) and  j > 0):
            
            if (i % len(a),j) in visited:
                break
            visited.add((i % len(a),j))
            
            if i % len(a) == 0 :
                temp += 1
                
            if a[i % len(a)] == b[j]:
                i , j = i + 1, j + 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lsp[j-1]

            if j == len(b):
                return temp
                
        return -1
