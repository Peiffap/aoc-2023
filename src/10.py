part = 2

import numpy as np

fo = open("../data/10.txt", "r")
f = list(fo)
fo.close()

if part == 1:
    cnt = 0
    grid = []
    lx, ly = 0, 0
    x, y = 0, 0

    for i, l in enumerate(f):
        grid.append([i for i in l.strip()])
        if 'S' in grid[-1]:
            y, x = i, grid[i].index('S')
            ly = y
            lx = x
    while True:
        #print(cnt, x, y, grid[y][x])
        nlx = x
        nly = y
        if grid[y][x] == 'S':
            if cnt != 0:
                break
            x += 1
        elif grid[y][x] == '-':
            if lx == x - 1:
                x += 1
            else:
                x -= 1
        elif grid[y][x] == '|':
            if ly == y - 1:
                y += 1
            else:
                y -= 1
        elif grid[y][x] == 'J':
            if lx == x - 1:
                y -= 1
            else:
                x -= 1
        elif grid[y][x] == '7':
            if lx == x - 1:
                y += 1
            else:
                x -= 1
        elif grid[y][x] == 'L':
            if lx == x + 1:
                y -= 1
            else:
                x += 1
        elif grid[y][x] == 'F':
            if lx == x + 1:
                y += 1
            else:
                x += 1
        
        lx = nlx
        ly = nly
        
        cnt += 1

    print(cnt // 2)
elif part == 2:
    cnt = 0
    grid = []
    lx, ly = 0, 0
    x, y = 0, 0

    for i, l in enumerate(f):
        grid.append([i for i in l.strip()])
        if 'S' in grid[-1]:
            y, x = i, grid[i].index('S')
            ly = y
            lx = x
    loop = [(y, x)]
    while True:
        nlx = x
        nly = y
        if grid[y][x] == 'S':
            if cnt != 0:
                break
            x += 1 # hardcoded from inspecting my input
        elif grid[y][x] == '-':
            if lx == x - 1:
                x += 1
            else:
                x -= 1
        elif grid[y][x] == '|':
            if ly == y - 1:
                y += 1
            else:
                y -= 1
        elif grid[y][x] == 'J':
            if lx == x - 1:
                y -= 1
            else:
                x -= 1
        elif grid[y][x] == '7':
            if lx == x - 1:
                y += 1
            else:
                x -= 1
        elif grid[y][x] == 'L':
            if lx == x + 1:
                y -= 1
            else:
                x += 1
        elif grid[y][x] == 'F':
            if lx == x + 1:
                y += 1
            else:
                x += 1
        
        lx = nlx
        ly = nly

        cnt += 1

        loop.append((y, x))

    # if we are inside/outside the loop, we must always be an odd/even number of crossings from both sides of the grid
    # if we "follow" an edge that goes back in the direction it came from, it counts as 2 crossings
    # otherwise, it counts as one
    s = 0
    for i in range(len(grid)):
        ccnt = 0
        n_crossings = []
        for x in range(len(grid[i])):
            # print(i, x)
            if (i, x) in loop:
                if grid[i][x] == '|':
                    ccnt += 1
                elif grid[i][x] == 'F':
                    ccnt += 1
                    d = 'up'
                elif grid[i][x] == 'J' and d == 'down':
                        ccnt += 1
                elif grid[i][x] == 'L':
                    ccnt += 1
                    d = 'down'
                elif grid[i][x] == '7' and d == 'up':
                    ccnt += 1
                elif grid[i][x] == 'S': # hardcoded from inspecting my input
                    ccnt += 1
                    d = 'down'
                n_crossings.append(0)
            else:
                n_crossings.append(ccnt % 2)
        s += sum(n_crossings)

    print(s)


   