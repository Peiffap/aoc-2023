import heapq

fo = open("../data/21.txt", "r")
f = list(fo)
fo.close()

grid = []
for i, l in enumerate(f):
    l = l.strip()
    grid.append(list(l))
    if 'S' in l:
        spos = (i, l.find('S'))

q = [(0, spos[0], spos[1])]

while True:
    state = heapq.heappop(q)
    if state[0] == 64:
        print(len(q) + 1)
        break
    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        npos = (state[1] + d[0], state[2] + d[1])
        if 0 <= npos[0] < len(grid) and 0 <= npos[1] < len(grid[0]) and grid[npos[0]][npos[1]] in ['S', '.']:
            ns = (state[0] + 1, npos[0], npos[1])
            if not ns in q:
                heapq.heappush(q, ns)

q = [(0, spos[0], spos[1])]
visited = set()
vo = 0
ve = 0
c = -1
v0 = -1
v1 = -1
v2 = -1
lg = len(grid)
offset = spos[0]

# every lg steps, the number of possible positions f(n) increases linearly (because of the . along the row and col of S)
# define g(m) = f(n + m * lg)
# this means that f(n), f(n + lg), f(n + 2lg), ... = g(0), g(1), g(2), ... is a quadratic
# next, we observe that 26501365 = 65 + 131 * 202300, and thus that f(26501365) = g(202300)
# we record f(65), f(65 + 131), and f(65 + 131 * 2), then interpolate this to find the solution at the goal
while True:
    state = q[0]
    q = q[1:]
    visited.add((state[1], state[2]))
    if state[0] > c:
        if state[0] % 2 == 0:
            ve += len(q) + 1
        else:
            vo += len(q) + 1
        c += 1
    if state[0] == offset:
        v0 = vo if state[0] % 2 == 1 else ve
    if state[0] == offset + lg:
        v1 = vo if state[0] % 2 == 1 else ve
    elif state[0] == offset + 2 * lg:
        v2 = vo if state[0] % 2 == 1 else ve
        break
    for d in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        npos = (state[1] + d[0], state[2] + d[1])
        if not npos in visited and grid[npos[0] % len(grid)][npos[1] % len(grid[0])] in ['S', '.']:
            ns = (state[0] + 1, npos[0], npos[1])
            if not ns in q:
                q.append(ns)

# g(n) = an^2 + bn + c
# => g(0) = c
# => g(1) = a + b + c
# => g(2) = 4a + 2b + c
# we already have c = g(0)
# we then know that g(2) - c - 2(g(1) - c) = 2a, hence a = (g(2) - 2g(1)) / 2
# finally, b = g(1) - c - a
c = v0
a = (v2 - c - 2 * (v1 - c)) // 2
b = v1 - c - a
g = lambda n: a * n ** 2 + b * n + c
goal = 26501365
print(g(goal // lg))