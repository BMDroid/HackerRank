def repeatedString(s, n):
    a, b = divmod(n, len(s))
    return a * s.lower().count('a') + s[0:b].count('a')


if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print(result)
