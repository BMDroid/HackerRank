def checkMagazine(magazine, note):
    from collections import Counter
    dic = dict(Counter(magazine))
    for word in note:
        if dic.get(word, -1) <= 0:
            print('No')
            return False
        else:
            dic[word] -= 1
    print('Yes')
    return True


if __name__ == '__main__':
    magazine = 'ive got a lovely bunch of coconuts'.rstrip().split()
    note = 'ive got some coconuts'.rstrip().split()
    checkMagazine(magazine, note)
