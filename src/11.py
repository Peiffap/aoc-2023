fo = open("../data/11.txt", "r")
f = list(fo)
fo.close()

gals = []
emptyr = [1 for i in range(len(f))]
emptyc = [1 for i in range(len(f[0]))]

for j, l in enumerate(f):
    for i, x in enumerate(l.strip()):
        if x == '#':
            gals.append((i, j))
            emptyc[i] = 0
            emptyr[j] = 0

s1 = 0
s2 = 0
for i, g1 in enumerate(gals):
    for j, g2 in enumerate(gals[i + 1:]):
        g1x, g1y = g1
        g2x, g2y = g2
        s1 += abs(g1x - g2x) + abs(g1y - g2y) + 1 * (sum(emptyr[min(g1y, g2y): max(g1y, g2y)]) + sum(emptyc[min(g1x, g2x): max(g1x, g2x)]))
        s2 += abs(g1x - g2x) + abs(g1y - g2y) + 999999 * (sum(emptyr[min(g1y, g2y): max(g1y, g2y)]) + sum(emptyc[min(g1x, g2x): max(g1x, g2x)]))

print(s1)
print(s2)