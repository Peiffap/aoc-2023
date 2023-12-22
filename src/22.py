import numpy as np
from collections import defaultdict
from copy import deepcopy

fo = open("../data/22.txt", "r")
f = list(fo)
fo.close()

bricks = []
for l in f:
    l = l.strip()
    a, b = l.split('~')
    a = [int(i) for i in a.split(',')]
    b = [int(i) for i in b.split(',')]
    bricks.append(np.array(a + b))
    assert a[0] <= b[0]
    assert a[1] <= b[1]
    assert a[2] <= b[2]

bricks.sort(key=lambda t: t[2])

supported_by = defaultdict(list)
supports = defaultdict(list)
fixed_pos = []

def get_positions(brick):
    brick_dir = brick[3:] - brick[:3]
    s = sum(brick_dir)
    if s == 0:
        return [tuple(brick[:3])]
    brick_dir //= s
    brick_positions = []
    for p in range(s + 1):
        brick_positions.append(tuple(brick[:3] + p * brick_dir))
    return brick_positions

def can_fall(brick, i):
    if brick[2] == 1:
        return False
    brickpos = set(get_positions(brick - np.array([0, 0, 1, 0, 0, 1])))
    for j in range(i):
        bpos = fixed_pos[j]
        if brickpos.intersection(bpos) != set():
            supported_by[i].append(j)
            supports[j].append(i)
    return supported_by[i] == []

for i in range(len(bricks)):
    #print(i, len(bricks))
    while can_fall(bricks[i], i):
        bricks[i] -= np.array([0, 0, 1, 0, 0, 1])
    gp = get_positions(bricks[i])
    fixed_pos.append(set(gp))

cnt1 = 0
cnt2 = 0
will_fall = defaultdict(set)
for b in range(len(bricks)):
    #print(b, len(bricks))
    can_disintegrate = True
    for i in range(b + 1, len(bricks)):
        if supported_by[i] == [b]:
            can_disintegrate = False
            will_fall[b].add(i)
    if can_disintegrate:
        cnt1 += 1

for b in range(len(bricks)):
    #print(b, len(bricks))
    i = b + 1
    while i < len(bricks):
        if not i in will_fall[b] and supported_by[i] != []:
            all_in = True
            for s in supported_by[i]:
                if not s in will_fall[b]:
                    all_in = False
            if all_in:
                will_fall[b].add(i)
                i = b + 1
        i += 1
    cnt2 += len(will_fall[b])

print(cnt1)
print(cnt2)