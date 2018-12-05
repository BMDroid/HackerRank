def climbingLeaderboard(scores, alice):
    def _update(a, d):
        for s in d:
            if s < a:
                d[s] += 1
    import bisect
    d = {}
    lst = []
    d[scores[0]] = 1
    for i in range(1, len(scores)):
        if scores[i] < scores[i - 1]:
            d[scores[i]] = d[scores[i - 1]] + 1
    for a in alice:
        if d.get(a, 0) != 0:
            lst.append(d[a])
        else:
            scores.reverse()
            bisect.insort(scores, a)
            scores.reverse()
            ind = scores.index(a)
            if ind == 0:
                lst.append(1)
                d[a] = 1
            else:
                rank = d.get(scores[ind - 1]) + 1
                lst.append(rank)
                d[a] = rank
            _update(a, d)
    return lst


if __name__ == '__main__':
    s = '100 90 90 80 75 60'
    scores = list(map(int, s.split()))
    a = '50 65 77 90 102'
    alice = list(map(int, a.split()))
    l = climbingLeaderboard(scores, alice)
    print(l)
