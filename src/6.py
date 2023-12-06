part = 2

fo = open("../data/6.txt", "r")
f = list(fo)
fo.close()

if part == 1:
    times = [int(i) for i in f[0].split(': ')[1].split()]
    distances = [int(i) for i in f[1].split(': ')[1].split()]

    possibilities = 1
    for t, d in zip(times, distances):
        for i in range(1, t):
            if i * (t - i) > d:
                possibilities *= (t - 2 * i + 1)
                break

    print(possibilities)
elif part == 2:
    t = int(f[0].split(': ')[1].replace(' ', ''))
    d = int(f[1].split(': ')[1].replace(' ', ''))

    for i in range(1, t):
        if i * (t - i) > d:
            print(t - 2 * i + 1)
            break