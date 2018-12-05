# https://www.hackerrank.com/challenges/electronics-shop/problem
def getMoneySpent(keyboards, drives, b):
    if min(keyboards) + min(drives) > b:
        print(-1)
        return -1

    maxPrice = 0
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            price = keyboards[i] + drives[j]
            if price < b:
                maxPrice = max(maxPrice, price)
            elif price == b:
                maxPrice = b
                break
    print(maxPrice)
    return maxPrice
