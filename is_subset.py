def is_subset(inputStr):
    a = []
    b = []
    for i, line in enumerate(inputStr):
        if i != 0 and i % 2 == 0 and i % 4 != 0:
            a = list(map(int, line.rstrip().split()))
            a = set(a)
        if i != 0 and i % 4 == 0:
            b = list(map(int, line.rstrip().split()))
            b = set(b)
            print(b.intersection(a) == a)


if __name__ == '__main__':
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    is_subset(lines)
