from collections import defaultdict

part = 2

f = open("../data/3.txt", "r")
s = 0
mat = []

if part == 1:
    symbs = set()

    for i, l in enumerate(f):
        l = l.strip()
        mat.append([])
        mat[i] = []
        for c in l:
            mat[i].append(c)
            if not c.isdigit() and c != '.':
                symbs.add(c)

    def find_symbol(x, y1, y2):
        for i in range(max(0, x - 1), min(x + 2, len(mat))):
            for j in range(max(0, y1 - 1), min(y2 + 2, len(mat[i]))):
                if mat[i][j] in symbs:
                    return True
        return False

    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[i]):
            if mat[i][j].isdigit():
                for k in range(j, len(mat[i])):
                    if not mat[i][k].isdigit():
                        if find_symbol(i, j, k - 1):
                            s += sum([10**i * int(a) for i, a in enumerate(mat[i][j:k][::-1])])
                        j = k
                        break
                    elif k == len(mat[i]) - 1:
                        if find_symbol(i, j, k):
                            s += sum([10**i * int(a) for i, a in enumerate(mat[i][j:][::-1])])
                        j = k + 1
            else:
                j += 1
        i += 1

    print(s)
elif part == 2:
    for i, l in enumerate(f):
        l = l.strip()
        mat.append([])
        mat[i] = []
        for c in l:
            mat[i].append(c)

    asterisks = defaultdict(list)

    def find_asterisk(x, y1, y2, num):
        for i in range(max(0, x - 1), min(x + 2, len(mat))):
            for j in range(max(0, y1 - 1), min(y2 + 2, len(mat[i]))):
                if mat[i][j] == '*':
                    asterisks[f"{i}, {j}"].append(num)

    i = 0
    while i < len(mat):
        j = 0
        while j < len(mat[i]):
            if mat[i][j].isdigit():
                for k in range(j, len(mat[i])):
                    if not mat[i][k].isdigit():
                        find_asterisk(i, j, k - 1, sum([10**i * int(a) for i, a in enumerate(mat[i][j:k][::-1])]))
                        j = k
                        break
                    elif k == len(mat[i]) - 1:
                        find_asterisk(i, j, k, sum([10**i * int(a) for i, a in enumerate(mat[i][j:][::-1])]))
                        j = k + 1
            else:
                j += 1
        i += 1

    for k, v in asterisks.items():
        if len(v) == 2:
            s += v[0] * v[1]

    print(s)
f.close()