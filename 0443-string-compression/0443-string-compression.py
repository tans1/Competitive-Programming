class Solution:
    def compress(self, chars: List[str]) -> int:
        res = []
        temp = chars[0]
        cnt = 0
        
        for i in range(len(chars)):
            if chars[i] == temp:
                cnt += 1
            else:
                if cnt > 1:
                    res += [temp] + list(str(cnt))
                else:
                    res += [temp]
                cnt = 1
                temp = chars[i]
        if cnt > 1:
            res += [temp] + list(str(cnt))
        else:
            res += [temp]
        
        while len(chars) > 0:
            del chars[0]
        for x in res:
            chars.append(x)
        return len(res)