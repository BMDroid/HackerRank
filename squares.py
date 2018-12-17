# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign

import math


def squares(a, b):
    counter = 0
    root = int(math.sqrt(a))
    sqr = root ** 2
    while sqr <= b:
        if sqr >= a:
            counter += 1
        root += 1
        sqr = root ** 2
    return counter
