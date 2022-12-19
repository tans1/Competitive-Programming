def swap_case(s):
    lst = list(s)
    for i, v in enumerate(lst):
        if v == v.upper():
            lst[i] = v.lower()
        else:
            lst[i] = v.upper()
    return ''.join(lst)

if __name__ == '__main__':
