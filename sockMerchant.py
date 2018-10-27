def sockMerchant(n, ar):
    from collections import Counter
    c = Counter(ar)
    pairs = 0
    for i in c:
        pairs += c[i] // 2
    return pairs


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print(result)
