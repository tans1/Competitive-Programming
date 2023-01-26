#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        j = i
        n = len(arr)
        
        while i < n:
            if arr[i] < arr[j]:
                j = i
            i += 1
        return j
        
    def selectionSort(self, arr,n):
        #code here
        for i in range(n-1):
            j = self.select(arr,i+1)
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        return arr
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends