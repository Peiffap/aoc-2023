import numpy as np
from collections import defaultdict

fo = open("../data/20.txt", "r")
f = list(fo)
fo.close()

ff = {}
c = {}
broadcaster = []

for l in f:
    l = l.strip()
    if l[0] == 'b':
        broadcaster = l.split(' -> ')[1].split(', ')
    elif l[0] == '%':
        n, o = l.split(' -> ')
        o = o.split(', ')
        ff[n[1:]] = [0, o]
    else:
        n, o = l.split(' -> ')
        o = o.split(', ')
        c[n[1:]] = {'in': [], 'out': o}

for f in ff:
    for o in ff[f][1]:
        if o in c:
            c[o]['in'].append([f, 0])

for co in c:
    for o in c[co]['out']:
        if o in c:
            c[o]['in'].append([co, 0])

q = []
prev = {}
count = defaultdict(int)
vr_times = []

cnt = [0, 0]

def send(dest, inp, sender, i):
    if dest == 'broadcaster':
        for ib in broadcaster:
            q.append((ib, inp, dest))
    elif dest == 'output' or dest == 'rx':
        return
    elif dest in ff:
        if inp == 0:
            if ff[dest][0] == 0:
                ff[dest][0] = 1
                for iff in ff[dest][1]:
                    q.append((iff, 1, dest))
            else:
                ff[dest][0] = 0
                for iff in ff[dest][1]:
                    q.append((iff, 0, dest))
    else:
        for t in c[dest]['in']:
            if t[0] == sender:
                t[1] = inp
                if inp == 0:
                    if dest in prev and count[dest] == 2 and dest in [a[0] for a in c['vr']['in']]:
                        vr_times.append(i - prev[dest])
                    count[dest] += 1
                    prev[dest] = i
                break
        if all(a[1] == 1 for a in c[dest]['in']):
            for o in c[dest]['out']:
                q.append((o, 0, dest))
        else:
            for o in c[dest]['out']:
                q.append((o, 1, dest))

i = 0
# is_back = sum(ff[f][0] for f in ff) + sum([sum([t[1] for t in c[o]['in']]) for o in c]) == 0
while True:
    i += 1
    q = [('broadcaster', 0, 'button')]
    while q:
        n, p, s = q[0]
        q = q[1:]
        send(n, p, s, i)
        cnt[p] += 1
    if i == 1000:
        print(cnt[0] * cnt[1])
    if len(vr_times) == len(c['vr']['in']):
        v = 1
        for vrt in vr_times:
            v = np.lcm(v, vrt)
        print(v)
        break

