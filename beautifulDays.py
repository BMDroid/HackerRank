# https: // www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem?utm_campaign = challenge-recommendation & utm_medium = email & utm_source = 24-hour-campaign


def beautifulDays(i, j, k):
    lst = list(range(i, j + 1))
    return len(list(filter(lambda x: abs(x - int(str(x)[::-1])) % k == 0, lst)))
