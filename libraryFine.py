# https://www.hackerrank.com/challenges/library-fine/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign
def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = [10000, 500, 15]
    lst = [y1 - y2, m1 - m2, d1 - d2]
    due = list(map(lambda x: x > 0, lst))
    for i in range(3):
        if due[i] and lst[i] > 0:
            return fine[i] * lst[i]
        if lst[i] < 0:
            return 0
    return 0

if __name__ == '__main__':
    d1 = 31
    m1 = 8  
    y1 = 2004
    d2 = 20
    m2 = 1
    y2 = 2004
    print(libraryFine(d1, m1, y1, d2, m2, y2))