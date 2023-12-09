part = 2

import numpy as np

fo = open("../data/9.txt", "r")
f = list(fo)
fo.close()

s = 0

for l in f:
    vals = np.array([int(i) for i in l.strip().split()])
    difs = {}
    i = 0
    while np.sum(np.dot(vals, vals)) != 0:
        difs[i] = vals
        i += 1
        vals = np.array([i - j for i, j in zip(vals[1:], vals[:-1])])
    difs[i] = vals

    if part == 1:
        for j in range(i):
            s += difs[j][-1]

    elif part == 2:
        ind = list(range(i)[::-1])
        for j in ind:
            nv = difs[j][0] - difs[j + 1][0]
            difs[j] = np.array([nv] + difs[j])
            s += nv

print(s)

   