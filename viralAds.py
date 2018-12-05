def viralAdvertising(n):
    numSum = 0
    num = 5
    for i in range(n):
        numSum += (num // 2)
        num = (num // 2) * 3
    return numSum

if __name__ == '__main__':
    n = 3
    print(viralAdvertising(n))