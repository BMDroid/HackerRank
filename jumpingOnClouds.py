def jumpingOnClouds(c):
    if len(c) == 1:
        return 0
    if len(c) == 2:
        return 1
    if c[2] != 1:
        return 1 + jumpingOnClouds(c[2::])
    else:
        return 1 + jumpingOnClouds(c[1::])


if __name__ == '__main__':
    n = 6
    c = list(map(int, '0 0 1 0 0 1 0'.split()))
    result = jumpingOnClouds(c)
    print(result)
