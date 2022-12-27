# Enter your code here. Read input from STDIN. Print output to STDOUT


def findUnion(eng,frn):
    english = set(eng)
    french = set(frn)
    intersection = english.intersection(french)
    union = len(english) + len(french) - len(intersection)
    return union


m = int(input())
eng = input().split()
n = int(input())
frn = input().split()

print(findUnion(eng,frn))
