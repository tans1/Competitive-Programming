# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
eng = input().split()
m = int(input())
frn = input().split()
english = set(eng)
french = set(frn)
diff = english - french
print(len(diff))
