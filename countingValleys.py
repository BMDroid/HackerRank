def countingValleys(n, s):
    height = 0
    lowest = 0
    counter = 0
    for i in range(n):
        if s[i] == 'U':
            height += 1
        else:
            height -= 1
        lowest = min(lowest, height)
        if lowest < 0 and height == 0:
            counter += 1
            lowest = 0
    return counter


if __name__ == '__main__':
    n = 8
    s = 'UDDDUDUU'
    print(countingValleys(n, s))
