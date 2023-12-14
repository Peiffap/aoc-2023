import numpy as np

fo = open("../data/14.txt", "r")
f = list(fo)
fo.close()

grid = []

for l in f:
    grid.append(list(l.strip()))

s = 0
for i in range(len(grid[0])):
    col = ''.join([r[i] for r in grid])
    os = 0
    lasth = -1
    for j, c in enumerate(col):
        if c == 'O':
            os += 1
        elif c == '#':
            cou = os
            s += (len(grid) - 1 - lasth) * (len(grid) - 1 - lasth + 1) // 2 - ((len(grid) - 1 - lasth - os) * (len(grid) - 1 - lasth - os + 1) // 2)
            os = 0
            lasth = j
        if c != '#' and j == len(col) - 1:
            cou = os
            s += (len(grid) - 1 - lasth) * (len(grid) - 1 - lasth + 1) // 2 - ((len(grid) -1 - lasth - os) * (len(grid) - 1 - lasth - os + 1) // 2)
            os = 0
            lasth = j

print(s)

ls = {}
states = [0]

grid = np.array(grid)

n = 1
while True:
    for i in range(len(grid[0])):
        lasth = -1
        for j, c in enumerate(grid[:, i]):
            if c == '#':
                grid[lasth + 1:j, i][::-1].sort()
                lasth = j
            elif j == len(col) - 1:
                grid[lasth + 1:, i][::-1].sort()

    for i in range(len(grid)):
        lasth = -1
        for j, c in enumerate(grid[i]):
            if c == '#':
                grid[i, lasth + 1:j][::-1].sort()
                lasth = j
            elif j == len(col) - 1:
                grid[i, lasth + 1:][::-1].sort()

    for i in range(len(grid[0])):
        lasth = -1
        for j, c in enumerate(grid[:, i]):
            if c == '#':
                grid[lasth + 1:j, i].sort()
                lasth = j
            elif j == len(col) - 1:
                grid[lasth + 1:, i].sort()

    for i in range(len(grid)):
        lasth = -1
        for j, c in enumerate(grid[i]):
            if c == '#':
                grid[i, lasth + 1:j].sort()
                lasth = j
            elif j == len(col) - 1:
                grid[i, lasth + 1:].sort()

    tgrid = tuple([tuple(r) for r in grid])
    states.append(tgrid)
    if tgrid in ls.keys():
        offset = ls[tgrid]
        period = n - ls[tgrid]

        s = 0
        tgrid = states[offset + ((1000000000 - offset) % period)]
        for i in range(len(tgrid[0])):
            col = ''.join([r[i] for r in tgrid])
            for j, c in enumerate(col):
                if c == 'O':
                    s += len(grid) - j
        print(s)
        break
    else:
        ls[tgrid] = n
    n += 1