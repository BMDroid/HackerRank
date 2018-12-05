# https://www.hackerrank.com/challenges/circular-array-rotation/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def circularArrayRotation(a, k, queries):
    length = len(a)
    b = [None] * length
    for i, n in enumerate(a):
        idx = (i + k) % length
        b[idx] = n
    for j in queries:
        print(b[j])
