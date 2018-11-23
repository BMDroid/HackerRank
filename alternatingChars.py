def alternatingCharacters(s):
    if len(s) <= 1:
        return 0
    if s[0] == s[1]:
        return 1 + alternatingCharacters(s[1::])
    return alternatingCharacters(s[1::])
