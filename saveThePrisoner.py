# https://www.hackerrank.com/challenges/save-the-prisoner/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign&h_r=next-challenge&h_v=zen
def saveThePrisoner(n, m, s):
    r = m % n
    if r == 0:
        if s != 1:
            return s - 1
        return n
    r += s - 1
    if r > n:
        return r % n
    return r
