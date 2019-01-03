def appendAndDelete(s, t, k):
    startIdx = 0
    endIdx = len(t) - 1
    steps = 0
    if len(s) < len(t):
        endIdx = len(s)
        steps = len(t) - endIdx
    elif len(s) > len(t):
        steps = len(s) - len(t)
    for i in range(0, endIdx):
        if s[i] != t[i]:
            startIdx = i
            break
    print(steps, startIdx, endIdx)
    if startIdx == 0 and s[0] != t[0]:
        steps += endIdx - startIdx
    elif startIdx == 0 and s[0] == t[0]:
        steps += startIdx
    else:
        steps += 2 * (endIdx - startIdx + 1)
    print(steps)
    print('Yes' if steps <= k else 'No')

if __name__ == '__main__':
    s = 'y'
    t = 'yu'
    k = 2
    appendAndDelete(s, t, k)
