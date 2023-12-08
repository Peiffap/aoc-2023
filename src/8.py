part = 2

import queue
import numpy as np

fo = open("../data/8.txt", "r")
f = list(fo)
fo.close()

instructions = f[0].strip()

moves = {}

if part == 1:
    for l in f[2:]:
        l = l.strip()
        moves[l[:3]] = {"L": l[7:10], 'R': l[12:15]}
        print(l)

    node = 'AAA'
    cnt = 0
    while node != 'ZZZ':
        node = moves[node][instructions[cnt % len(instructions)]]
        cnt += 1
    print(cnt)
elif part == 2:
    # lcm only works because loops reset to 0
    q = []
    nodes = set()
    for l in f[2:]:
        l = l.strip()
        moves[l[:3]] = {"L": l[7:10], 'R': l[12:15]}
        nodes.add(l[:3])

    for node in nodes:
        if node[-1] == 'A':
            q.append(node)

    cnt = 0
    ndones = [0] * len(q)
    periods = [0] * len(q)
    while True:
        for i in range(len(q)):
            q[i] = moves[q[i]][instructions[cnt % len(instructions)]]
        cnt += 1
        done = True
        for i in range(len(q)):
            if q[i][-1] != 'Z':
                done = False
            else:
                ndones[i] = min(2, ndones[i] + 1)
                if ndones[i] == 2 and periods[i] == 0:
                    periods[i] = cnt // 2
        
        if sum(ndones) == 2 * len(ndones):
            lc = 1
            for p in periods:
                lc = np.lcm(lc, p)
            print(lc)
            quit()

   