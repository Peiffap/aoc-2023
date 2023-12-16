fo = open("../data/16.txt", "r")
f = list(fo)
fo.close()

grid = []

for r in f:
    r = r.strip()
    grid.append(list(r))

beamcounts = []
for i in range(len(grid)):
    beamcounts.append([])
    for j in range(len(grid[0])):
        beamcounts[i].append(set())


q = [(0, 0, (0, 1))] # beams to consider (row, col, direction)

while q:
    beam = q[0]
    q = q[1:]
    while True:
        if not 0 <= beam[0] < len(grid) or not 0 <= beam[1] < len(grid[0]):
            break
        if beam[2] in beamcounts[beam[0]][beam[1]]:
            break
        beamcounts[beam[0]][beam[1]].add(beam[2])
        if grid[beam[0]][beam[1]] == '.':
            beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])
        elif grid[beam[0]][beam[1]] == '|':
            if beam[2] == (1, 0) or beam[2] == (-1, 0):
                beam = (beam[0] + beam[2][0], beam[1], beam[2])
            else:
                b1 = (beam[0] - 1, beam[1], (-1, 0))
                b2 = (beam[0] + 1, beam[1], (1, 0))
                q.append(b1)
                q.append(b2)
                break
        elif grid[beam[0]][beam[1]] == '-':
            if beam[2] == (0, 1) or beam[2] == (0, -1):
                beam = (beam[0], beam[1] + beam[2][1], beam[2])
            else:
                b1 = (beam[0], beam[1] - 1, (0, -1))
                b2 = (beam[0], beam[1] + 1, (0, 1))
                q.append(b1)
                q.append(b2)
                break
        elif grid[beam[0]][beam[1]] == '/':
            if beam[2] == (0, 1):
                beam = (beam[0] - 1, beam[1], (-1, 0))
            elif beam[2] == (-1, 0):
                beam = (beam[0], beam[1] + 1, (0, 1))
            elif beam[2] == (0, -1):
                beam = (beam[0] + 1, beam[1], (1, 0))
            else:
                beam = (beam[0], beam[1] - 1, (0, -1))
        else:
            if beam[2] == (0, 1):
                beam = (beam[0] + 1, beam[1], (1, 0))
            elif beam[2] == (1, 0):
                beam = (beam[0], beam[1] + 1, (0, 1))
            elif beam[2] == (0, -1):
                beam = (beam[0] - 1, beam[1], (-1, 0))
            else:
                beam = (beam[0], beam[1] - 1, (0, -1))

s = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if len(beamcounts[i][j]) > 0:
            s += 1
print(s)

beamcounts = []
for i in range(len(grid)):
    beamcounts.append([])
    for j in range(len(grid[0])):
        beamcounts[i].append(set())

best = s

for startindex in range(len(grid)):
    beamcounts = []
    for i in range(len(grid)):
        beamcounts.append([])
        for j in range(len(grid[0])):
            beamcounts[i].append(set())

    st = (startindex, 0, (0, 1))
    q = [st] # beams to consider (row, col, direction)

    while q:
        beam = q[0]
        q = q[1:]
        while True:
            if not 0 <= beam[0] < len(grid) or not 0 <= beam[1] < len(grid[0]):
                break
            if beam[2] in beamcounts[beam[0]][beam[1]]:
                break
            beamcounts[beam[0]][beam[1]].add(beam[2])
            if grid[beam[0]][beam[1]] == '.':
                beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])
            elif grid[beam[0]][beam[1]] == '|':
                if beam[2] == (1, 0) or beam[2] == (-1, 0):
                    beam = (beam[0] + beam[2][0], beam[1], beam[2])
                else:
                    b1 = (beam[0] - 1, beam[1], (-1, 0))
                    b2 = (beam[0] + 1, beam[1], (1, 0))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '-':
                if beam[2] == (0, 1) or beam[2] == (0, -1):
                    beam = (beam[0], beam[1] + beam[2][1], beam[2])
                else:
                    b1 = (beam[0], beam[1] - 1, (0, -1))
                    b2 = (beam[0], beam[1] + 1, (0, 1))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '/':
                if beam[2] == (0, 1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                elif beam[2] == (-1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))
            else:
                if beam[2] == (0, 1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                elif beam[2] == (1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(beamcounts[i][j]) > 0:
                s += 1

    if s > best:
        best = s

    beamcounts = []
    for i in range(len(grid)):
        beamcounts.append([])
        for j in range(len(grid[0])):
            beamcounts[i].append(set())

    st = (startindex, len(grid[0]) - 1, (0, -1))
    q = [st] # beams to consider (row, col, direction)

    while q:
        beam = q[0]
        q = q[1:]
        while True:
            if not 0 <= beam[0] < len(grid) or not 0 <= beam[1] < len(grid[0]):
                break
            if beam[2] in beamcounts[beam[0]][beam[1]]:
                break
            beamcounts[beam[0]][beam[1]].add(beam[2])
            if grid[beam[0]][beam[1]] == '.':
                beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])
            elif grid[beam[0]][beam[1]] == '|':
                if beam[2] == (1, 0) or beam[2] == (-1, 0):
                    beam = (beam[0] + beam[2][0], beam[1], beam[2])
                else:
                    b1 = (beam[0] - 1, beam[1], (-1, 0))
                    b2 = (beam[0] + 1, beam[1], (1, 0))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '-':
                if beam[2] == (0, 1) or beam[2] == (0, -1):
                    beam = (beam[0], beam[1] + beam[2][1], beam[2])
                else:
                    b1 = (beam[0], beam[1] - 1, (0, -1))
                    b2 = (beam[0], beam[1] + 1, (0, 1))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '/':
                if beam[2] == (0, 1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                elif beam[2] == (-1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))
            else:
                if beam[2] == (0, 1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                elif beam[2] == (1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(beamcounts[i][j]) > 0:
                s += 1

    if s > best:
        best = s

    beamcounts = []
    for i in range(len(grid)):
        beamcounts.append([])
        for j in range(len(grid[0])):
            beamcounts[i].append(set())

    st = (0, startindex, (1, 0))
    q = [st] # beams to consider (row, col, direction)

    while q:
        beam = q[0]
        q = q[1:]
        while True:
            if not 0 <= beam[0] < len(grid) or not 0 <= beam[1] < len(grid[0]):
                break
            if beam[2] in beamcounts[beam[0]][beam[1]]:
                break
            beamcounts[beam[0]][beam[1]].add(beam[2])
            if grid[beam[0]][beam[1]] == '.':
                beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])
            elif grid[beam[0]][beam[1]] == '|':
                if beam[2] == (1, 0) or beam[2] == (-1, 0):
                    beam = (beam[0] + beam[2][0], beam[1], beam[2])
                else:
                    b1 = (beam[0] - 1, beam[1], (-1, 0))
                    b2 = (beam[0] + 1, beam[1], (1, 0))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '-':
                if beam[2] == (0, 1) or beam[2] == (0, -1):
                    beam = (beam[0], beam[1] + beam[2][1], beam[2])
                else:
                    b1 = (beam[0], beam[1] - 1, (0, -1))
                    b2 = (beam[0], beam[1] + 1, (0, 1))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '/':
                if beam[2] == (0, 1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                elif beam[2] == (-1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))
            else:
                if beam[2] == (0, 1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                elif beam[2] == (1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(beamcounts[i][j]) > 0:
                s += 1

    if s > best:
        best = s

    beamcounts = []
    for i in range(len(grid)):
        beamcounts.append([])
        for j in range(len(grid[0])):
            beamcounts[i].append(set())

    st = (len(grid) - 1, startindex, (-1, 0))
    q = [st] # beams to consider (row, col, direction)

    while q:
        beam = q[0]
        q = q[1:]
        while True:
            if not 0 <= beam[0] < len(grid) or not 0 <= beam[1] < len(grid[0]):
                break
            if beam[2] in beamcounts[beam[0]][beam[1]]:
                break
            beamcounts[beam[0]][beam[1]].add(beam[2])
            if grid[beam[0]][beam[1]] == '.':
                beam = (beam[0] + beam[2][0], beam[1] + beam[2][1], beam[2])
            elif grid[beam[0]][beam[1]] == '|':
                if beam[2] == (1, 0) or beam[2] == (-1, 0):
                    beam = (beam[0] + beam[2][0], beam[1], beam[2])
                else:
                    b1 = (beam[0] - 1, beam[1], (-1, 0))
                    b2 = (beam[0] + 1, beam[1], (1, 0))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '-':
                if beam[2] == (0, 1) or beam[2] == (0, -1):
                    beam = (beam[0], beam[1] + beam[2][1], beam[2])
                else:
                    b1 = (beam[0], beam[1] - 1, (0, -1))
                    b2 = (beam[0], beam[1] + 1, (0, 1))
                    q.append(b1)
                    q.append(b2)
                    break
            elif grid[beam[0]][beam[1]] == '/':
                if beam[2] == (0, 1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                elif beam[2] == (-1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))
            else:
                if beam[2] == (0, 1):
                    beam = (beam[0] + 1, beam[1], (1, 0))
                elif beam[2] == (1, 0):
                    beam = (beam[0], beam[1] + 1, (0, 1))
                elif beam[2] == (0, -1):
                    beam = (beam[0] - 1, beam[1], (-1, 0))
                else:
                    beam = (beam[0], beam[1] - 1, (0, -1))

    s = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if len(beamcounts[i][j]) > 0:
                s += 1

    if s > best:
        best = s
print(best)

