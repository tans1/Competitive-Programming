#User function Template for python3

class Solution: 
    def select(self, arr, i):
        j = i
        n = len(arr)
        while i < n:
            if arr[i] < arr[j]:
                j = i
            i += 1
        return j
        
    def selectionSort(self, arr,n):
        for i in range(n-1):
            j = self.select(arr,i+1)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        return arr
        
