class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = 0
        
        for wrd in words:
            max_len = max(max_len,len(wrd))
        
        all_words_list = []
        for wrd in words:
            wrd_list = list(wrd)
            
            if len(wrd_list) < max_len:
                wrd_list.extend([' ']*(max_len - len(wrd_list)))
                
            all_words_list.append(wrd_list)
        
        lists = list(zip(*all_words_list))
        result = []
        
        for index in range(max_len):
            string = ''.join(lists[index])
            result.append(string.rstrip())
        
        return result
                