class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = n - 2
        while i >= 0 and arr[i] <= arr[i+1]:
            i -= 1
            
        if i >= 0:
            mx_index = i + 1
            for j in range(i+1,n):
                if arr[j] < arr[i] and arr[mx_index] < arr[j]:
                    mx_index = j
            
            arr[mx_index], arr[i] = arr[i], arr[mx_index]
        
        return arr
                    