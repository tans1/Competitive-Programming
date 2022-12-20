n = int(input())
words = []
for i in range(n):
    words.append(input())
dic = {}
for word in words:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] += 1

print(len(dic))
for i in list(dic.values()):
    print(i, end=" ")
