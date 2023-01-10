class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        ones_index = []
        
        for i in range(len(boxes)):
            if boxes[i] == '1': ones_index.append(i)
        
        for j in range(len(boxes)):
            temp = 0
            for ind in ones_index:
                temp += abs(ind - j)
            res.append(temp)
        
        return res
                
        
        
        # for i in range(len(boxes)):
        #     temp = 0
        #     for j in range(len(boxes)):
        #         if boxes[j] == '1':
        #             temp += abs(i-j)
        #     res.append(temp)
        # return res