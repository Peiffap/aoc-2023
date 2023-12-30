from collections import defaultdict
import heapq

fo = open("../data/23.txt", "r")
f = list(fo)
fo.close()

grid = []
for l in f:
    l = l.strip()
    grid.append(l)

starty = 0
endy = len(grid) - 1
startx = grid[starty].find('.')
endx = grid[endy].find('.')

m = -1

q = [(starty, startx, set())]
while q:
    e = q.pop()
    if e[0] == endy and e[1] == endx:
        m = max(m, len(e[2]))
    poss = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    if grid[e[0]][e[1]] == '<':
        poss = [[0, -1]]
    elif grid[e[0]][e[1]] == '>':
        poss = [[0, 1]]
    elif grid[e[0]][e[1]] == 'v':
        poss = [[1, 0]]
    elif grid[e[0]][e[1]] == '^':
        poss = [[-1, 0]]
    for d in poss:
        ny, nx = e[0] + d[0], e[1] + d[1]
        if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and not (ny, nx) in e[2] and grid[ny][nx] != '#':
            ns = e[2].copy()
            ns.add((e[0], e[1]))
            q.append((ny, nx, ns))

print(m)

imp = [(starty, startx), (endy, endx)]

def neigh(x, y):
    poss = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    cnt = 0
    for d in poss:
        ny = y + d[0]
        nx = x + d[1]
        if grid[ny][nx] != '#':
            cnt += 1
    return cnt

for y in range(1, len(grid) - 1):
    for x in range(1, len(grid[y]) - 1):
        if grid[y][x] == '.' and neigh(x, y) > 2:
            imp.append((y, x))

neighbors = defaultdict(list)

for index, t in enumerate(imp):
    q = [(t[0], t[1], set())]
    while q:
        e = q.pop()
        if (e[0], e[1]) in imp and not (e[0] == t[0] and e[1] == t[1]):
            neighbors[index].append((imp.index((e[0], e[1])), len(e[2])))
            neighbors[imp.index((e[0], e[1]))].append((index, len(e[2])))
            continue
        poss = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        for d in poss:
            ny, nx = e[0] + d[0], e[1] + d[1]
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and not (ny, nx) in e[2] and grid[ny][nx] != '#':
                ns = e[2].copy()
                ns.add((e[0], e[1]))
                q.append((ny, nx, ns))

for k in neighbors.keys():
    neighbors[k] = list(set(neighbors[k]))

ma = 0
q = [(0, [0])] # cost, path
while q:
    e = heapq.heappop(q)
    cost, path = e
    if path[-1] == 1:
        if cost > ma:
            #print(cost, path, len(q))
            ma = cost
        continue
    for neighb, weight in neighbors[path[-1]]:
        if not neighb in path:
            heapq.heappush(q, (cost + weight, path + [neighb]))

print(ma)