from sympy import Symbol, solve

fo = open("../data/24.txt", "r")
f = list(fo)
fo.close()

limit = [200000000000000, 400000000000000]

positions = []
velocities = []

for l in f:
    l = l.strip()
    p, v = l.split(' @ ')
    px, py, pz = [int(i) for i in p.split(', ')]
    vx, vy, vz = [int(i) for i in v.split(', ')]
    positions.append((px, py, pz))
    velocities.append((vx, vy, vz))

def compute_collision(i, j):
    px1, py1 = positions[i][:-1]
    px2, py2 = positions[j][:-1]
    vx1, vy1 = velocities[i][:-1]
    vx2, vy2 = velocities[j][:-1]

    if vy2 * vx1 == vy1 * vx2:
        return -1, -1, -1, -1

    t2 = (py1 + ((vy1 * (px2 - px1)) / vx1) - py2) / (vy2 - (vy1 * vx2) / vx1)
    t1 = (px2 - px1 + vx2 * t2) / vx1

    return t1, t2, px1 + vx1 * t1, py1 + vy1 * t1

cnt = 0
for i in range(len(positions) - 1):
    for j in range(i + 1, len(positions)):
        t1, t2, x, y = compute_collision(i, j)
        if t1 > 0 and t2 > 0 and limit[0] <= x <= limit[1] and limit[0] <= y <= limit[1]:
            cnt += 1

print(cnt)

xr = Symbol('xr', integer=True)
yr = Symbol('yr', integer=True)
zr = Symbol('zr', integer=True)
vxr = Symbol('vxr', integer=True)
vyr = Symbol('vyr', integer=True)
vzr = Symbol('vzr', integer=True)
t1 = Symbol('t1', integer=True)
t2 = Symbol('t2', integer=True)
t3 = Symbol('t3', integer=True)

x1, y1, z1 = positions[0]
x2, y2, z2 = positions[1]
x3, y3, z3 = positions[2]

vx1, vy1, vz1 = velocities[0]
vx2, vy2, vz2 = velocities[1]
vx3, vy3, vz3 = velocities[2]

equations = [x1 + vx1 * t1 - xr - vxr * t1,
             y1 + vy1 * t1 - yr - vyr * t1,
             z1 + vz1 * t1 - zr - vzr * t1,
             x2 + vx2 * t2 - xr - vxr * t2,
             y2 + vy2 * t2 - yr - vyr * t2,
             z2 + vz2 * t2 - zr - vzr * t2,
             x3 + vx3 * t3 - xr - vxr * t3,
             y3 + vy3 * t3 - yr - vyr * t3,
             z3 + vz3 * t3 - zr - vzr * t3]

s = solve(equations, xr, yr, zr, vxr, vyr, vzr, t1, t2, t3, dict=True)[0]
print(s[xr] + s[yr] + s[zr])