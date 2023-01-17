class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        i = 0
        while i < len(heights)-1:
            
            j = i
            min_index = j
            
            while j < len(heights):
                if heights[j] < heights[min_index]:
                    min_index = j
                j += 1

            heights[i], heights[min_index] = heights[min_index], heights[i]
            names[i], names[min_index] = names[min_index], names[i]
            
            i += 1

        names.reverse()
        
        return names
            # return sorted(names , key= lambda x: heights.index)
#         for i in range(len(heights)):
#             for  j in range(len(heights)-1):
#                 if heights[j] > heights[j+1]:
                    
#                     heights[j], heights[j+1] = heights[j+1], heights[j]
#                     names[j], names[j+1] = names[j+1], names[j]
        
#         names.reverse()
        # return names
    
    
        