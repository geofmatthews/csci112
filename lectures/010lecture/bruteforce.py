def anagramSolution3(s1, s2):
    return s1 in all_permutations(s2)


def all_permutations(s):
    if len(s) == 1:
        return [s]
    else:
        shorters = all_permutations(s[1:])
        longers = []
        for shorter in shorters:
            longers = longers + all_positions(s[0], shorter)
        return longers

def all_positions(c, s):
    strings = []
    for i in range(len(s)+1):
        strings.append(s[0:i] + c + s[i:])
    return strings


print(all_positions('X', 'abcd'))
print(all_permutations('abcd'))
print(anagramSolution3('abcd', 'dcba'))
print(anagramSolution3('abcd', 'dxba'))
