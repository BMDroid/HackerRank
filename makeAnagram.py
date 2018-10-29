# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings
def makeAnagram(a, b):
    s = set(a).intersection(set(b))
    return len(a) + len(b) - 2 * sum([min(a.count(c), b.count(c)) for c in s])


if __name__ == '__main__':
    a = input()
    b = input()
    res = makeAnagram(a, b)
