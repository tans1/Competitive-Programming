class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using hash map
        dct = {}
        for i in range(len(numbers)):
            if (numbers[i]) in dct:
                return [dct[numbers[i]] + 1, i+1]
            else:
                dct[target - numbers[i]] = i
        
        
        
        
        #using two pointer
        
        i = 0
        j = len(numbers)-1
        
        while i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            elif numbers[i] + numbers[j] < target:
                i += 1
            else:
                return [i+1,j+1]