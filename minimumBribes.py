# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumBribes(q):
    totalB = 0
    for i in range(len(q)):
        if q[i] > i + 1:
            b = q[i] - i - 1
            if b > 2:
                print('Too chaotic')
                return False
            totalB += b
    print(totalB)
    return True


if __name__ == '__main__':
    q = list(map(int, '1 2 5 3 7 8 6 4'.split()))
    minimumBribes(q)
