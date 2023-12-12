from itertools import groupby

fo = open("../data/12.txt", "r")
f = list(fo)
fo.close()

def generate_strings(s):
    if s.count('?') == 0:
        return [s]
    return [s.replace('?', '.', 1), s.replace('?', '#', 1)]

def count_springs(s):
    gr = groupby(s)
    cnts = []
    gr = [(label, sum(1 for _ in group)) for label, group in gr]
    for c, cnt in gr:
        if c == '#':
            cnts.append(cnt)
        if c == '?':
            return cnts
    return cnts


s = 0
li = []
for l in f:
    springs, vals = l.strip().split(' ')
    vals = [int(i) for i in vals.split(',')]

    cnt = 0
    to_check = [springs]
    while to_check:
        st = generate_strings(to_check[0])
        to_check = to_check[1:]
        if len(st) == 1:
            if count_springs(st[0]) == vals:
                cnt += 1
        else:
            for stri in st:
                cnts = count_springs(stri)
                if len(cnts) == 0:
                    to_check.append(stri)
                elif len(cnts) <= len(vals):
                    for i, c in enumerate(cnts):
                        if i < len(cnts) - 1 and c != vals[i]:
                            break
                        if i == len(cnts) - 1 and c <= vals[i]:
                            to_check.append(stri)
    s += cnt
print(s)

s = 0
for i, l in enumerate(f):
    springs, vals = l.strip().split(' ')
    vals = [int(i) for i in vals.split(',')]

    springs += '?'
    springs = springs + springs + springs + springs + springs
    springs = springs[:-1] + '.' # avoid edge cases
    vals = vals + vals + vals + vals + vals

    cnts = [[[0 for _ in range(len(springs) + 2)] for _ in range(len(vals) + 2)] for _ in range(len(springs) + 1)]
    cnts[0][0][0] = 1
    for p in range(len(springs)):
        for n in range(len(vals) + 1):
            for l in range(len(springs) + 1):
                if cnts[p][n][l] == 0:
                    continue
                if springs[p] == '#' or springs[p] == '?':
                    cnts[p + 1][n + (l == 0)][l + 1] += cnts[p][n][l]
                if (springs[p] == '.' or springs[p] == '?') and (l == 0 or l == vals[n - 1]):
                    cnts[p + 1][n][0] += cnts[p][n][l]

    s += cnts[len(springs)][len(vals)][0]
print(s)