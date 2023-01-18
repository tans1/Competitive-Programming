class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3 : return False
        i , j = 0 , len(arr)-1
        
        while i < len(arr) - 1 and arr[i] < arr[i+1]:
            i += 1
        while j > 1 and arr[j] < arr[j-1]:
            j -= 1
        
        if i == 0 or i != j or j == len(arr)-1:
            return False
        else:
            return True
        