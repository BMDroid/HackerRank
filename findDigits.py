# https://www.hackerrank.com/challenges/find-digits/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def findDigits(n):
    s = str(n)
    num = len(list(filter(lambda x: int(x) != 0 and n % int(x) == 0, s)))
    return num
