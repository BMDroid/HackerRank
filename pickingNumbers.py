# https://www.hackerrank.com/challenges/picking-numbers/problem


def pickingNumbers(a):
    # Write your code here
    from collections import Counter
    c = Counter(a)
    maxLen = 0
    for n in c:
        maxLen = max(maxLen, c.get(n - 1, 0) + c[n], c.get(n + 1, 0) + c[n])
    return maxLen
