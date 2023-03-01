#!/bin/python3

def arrayManipulation(n, queries):
    temp = [0 for _ in range(n + 1)]
    
    for query in queries:
        k = query[2]
            
        temp[query[0] - 1] += k
        temp[query[1]] -= k
    
    for i in range(1,len(temp)):
        temp[i] += temp[i-1]
        
    return max(temp)
