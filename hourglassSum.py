# https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def hourglassSum(arr):
    maxH = -9 * 7
    counter = 0
    while counter < 16:
        for i in range(len(arr[0]) - 2):
            j = counter // 4
            h = sum(arr[j][i: i + 3]) + arr[j + 1][i + 1] + \
                sum(arr[j + 2][i: i + 3])
            maxH = max(maxH, h)
            counter += 1
    return maxH


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
