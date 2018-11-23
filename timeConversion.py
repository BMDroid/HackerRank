def timeConversion(s):
    #
    # Write your code here.
    #
    ap = s[-2::]
    lst = list(map(int, s[0:-2].split(':')))
    if ap == 'AM':
        lst[0] = lst[0] % 12
    else:
        if lst[0] != 12:
            lst[0] = (lst[0] + 12) % 24
    return '{:02d}:{:02d}:{:02d}'.format(*lst)
