# https://www.hackerrank.com/challenges/permutation-equation/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def permutationEquation(p):
    d = dict(zip(p, range(1, len(p) + 1)))
    lst = [d[d[x]] for x in (range(1, len(p) + 1))]
    return lst
