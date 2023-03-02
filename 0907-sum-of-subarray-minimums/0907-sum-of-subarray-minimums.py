class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        next_minn = [n for _ in range(n)]
        stack = [n-1]
        
        for i in range(n-2,-1,-1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_minn[i] = stack[-1]
            stack.append(i)


        pre = [-1 for _ in range(n)]
        st = [0]
        
        for i in range(1,n):
            while st and arr[st[-1]] >= arr[i]:
                st.pop()
            if st:
                pre[i] = st[-1]
            st.append( i)


        res = 0
        for i in range(n):
            res += (arr[i] * (next_minn[i] - i) * (i - pre[i]))
        return res %  ((10 ** 9) + 7)
            
            