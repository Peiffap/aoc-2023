from collections import defaultdict

fo = open("../data/13.txt", "r")
f = list(fo)
fo.close()

grid = []

def find_even_pal(string):
    l = set()
    for m in range(len(string) // 2, 0, -1):
        for i in [0, len(string) - 2 * m]:
            if string[i:i + m] == string[i + m:i + 2 * m][::-1]:
                l.add((i, m))
    return l

def can_be_fixed(string, reflection):
    i, m = reflection
    seq1, seq2 = string[i:i + m], string[i + m:i + 2 * m][::-1]
    return sum(1 for a, b in zip(seq1, seq2) if a != b) <= 1

cnt = 0
f += ['done']

for l in f:
    if not l.strip() or l =='done':
        if grid:
            r = find_even_pal(grid[0])
            for row in grid[1:]:
                r = r.intersection(find_even_pal(row))
            if r:
                cnt += sum(list(r)[0])
            else:
                c = find_even_pal(''.join([grid[k][0] for k in range(len(grid))]))
                for j in range(1, len(grid[0])):
                    c = c.intersection(find_even_pal(''.join([grid[k][j] for k in range(len(grid))])))
                cnt += 100 * sum(list(c)[0])
        grid = []
    else:
        grid.append(l.strip())

print(cnt)

cnt = 0

for l in f:
    if not l.strip() or l =='done':
        if grid:
            cnts = defaultdict(list)
            rows = grid
            for i, row in enumerate(rows):
                pals = find_even_pal(row)
                for tup in pals:
                    cnts[tup].append(i)
            for reflection in cnts.keys():
                r = set(range(len(rows))) - set(cnts[reflection])
                if len(r) == 1 and can_be_fixed(rows[list(r)[0]], reflection):
                        cnt += sum(reflection)

            cnts = defaultdict(list)
            cols = [''.join([grid[k][j] for k in range(len(grid))]) for j in range(len(grid[0]))]
            for i, col in enumerate(cols):
                pals = find_even_pal(col)
                for tup in pals:
                    cnts[tup].append(i)
            for reflection in cnts.keys():
                c = set(range(len(cols))) - set(cnts[reflection])
                if len(c) == 1 and can_be_fixed(cols[list(c)[0]], reflection):
                        cnt += 100 * sum(reflection)
        grid = []
    else:
        grid.append(l.strip())

print(cnt)