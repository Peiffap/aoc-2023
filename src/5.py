part = 2

fo = open("../data/5.txt", "r")
f = list(fo)
fo.close()

if part == 1:
    vals = [int(i) for i in f[0].split()[1:]]
    done = [False] * len(vals)

    for l in f[2:]:
        l = l.strip()
        if l[-4:] == 'map:':
            done = [False] * len(vals)
        elif l != '':
            x1, x2, x3 = [int(i) for i in l.split()]
            for i in range(len(vals)):
                if not done[i] and x2 <= vals[i] < x2 + x3:
                    done[i] = True
                    vals[i] = x1 + vals[i] - x2

    print(min(vals))
elif part == 2:
    vals = [int(i) for i in f[0].split()[1:]]
    rs = []
    for i in range(0, len(vals), 2):
        rs.append((vals[i], vals[i] + vals[i + 1]))
    done = [False] * len(rs)

    for l in f[2:]:
        l = l.strip()
        if l[-4:] == 'map:':
            done = [False] * len(rs)
        elif l != '':
            x1, x2, x3 = [int(i) for i in l.split()]
            for i in range(len(rs)):
                if not done[i]:
                    s, e = rs[i]
                    """
                    x2    s       e       x2+x3    map s:e -> s-x2+x1:e-x2+x1
                    x2    s       x2+x3   e        map s:x2+x3 -> s-x2+x1:x1+x3, x2+x3:e
                    x2    x2+x3   s       e        do nothing
                    s     x2      e       x2+x3    map s:x2, x2:e -> x1:e-x2+x1
                    s     x2      x2+x3   e        map s:x2, x2:x2+x3 -> x1:x1+x3, x2+x3:e
                    s     e       x2      x2+x3    do nothing
                    """
                    if x2 <= s <= e < x2 + x3:
                        rs[i] = (s - x2 + x1, e - x2 + x1)
                        done[i] = True
                    elif x2 <= s < x2 + x3 <= e:
                        rs[i] = (x2 + x3, e)
                        done[i] = False
                        rs.append((s - x2 + x1, x1 + x3))
                        done.append(True)
                    elif s < x2 <= e < x2 + x3:
                        rs[i] = (s, x2)
                        done[i] = False
                        rs.append((x1, e - x2 + x1))
                        done.append(True)
                    elif s < x2 <= x2 + x3 <= e:
                        rs[i] = (s, x2)
                        done[i] = False
                        rs.append((x1, x1 + x3))
                        done.append(True)
                        rs.append((x2 + x3, e))
                        done.append(False)
    
    print(min([r[0] for r in rs]))