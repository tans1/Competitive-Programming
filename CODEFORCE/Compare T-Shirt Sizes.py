dic = {
    'S' : 0,
    'M' : 1,
    'L' : 2
    }
testcases = int(input())
for _ in range(testcases):
    a,b = input().split()
    if dic[a[-1]] > dic[b[-1]]:
        print('>')
    elif dic[a[-1]] < dic[b[-1]]:
        print('<')
    else:
        ax = a.count('X')
        bx = b.count('X')

        if a[-1] == 'S':  
            if ax > bx:
                print('<')
            elif ax < bx:
                print('>')
            else:
                print('=')
        else:
            if ax > bx:
                print('>')
            elif ax < bx:
                print('<')
            else:
                print('=')
