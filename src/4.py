part = 2

fo = open("../data/4.txt", "r")
f = list(fo)
fo.close()
s = 0

if part == 1:
    for l in f:
        l = l.strip()
        for i in range(len(l)):
            if l[i] == ':':
                l = l[i + 1:]
                break
        
        winning = set()
        mode = 0
        i = 0
        cnt = 0
        while i < len(l):
            if l[i:i+2] == ' |':
                mode = 1
                i += 2
            else:
                if mode == 0:
                    winning.add(int(l[i:i+3].strip()))
                elif mode == 1:
                    if int(l[i:i+3].strip()) in winning:
                        cnt += 1
                i += 3

        if cnt != 0:
            s += int(2 ** (cnt - 1))

    print(s)
elif part == 2:
    cards = [1] * len(f)

    for j, l in enumerate(f):
        l = l.strip()
        for i in range(len(l)):
            if l[i] == ':':
                l = l[i + 1:]
                break
        
        winning = set()
        mode = 0
        i = 0
        cnt = 0
        while i < len(l):
            if l[i:i+2] == ' |':
                mode = 1
                i += 2
            else:
                if mode == 0:
                    winning.add(int(l[i:i+3].strip()))
                elif mode == 1:
                    if int(l[i:i+3].strip()) in winning:
                        cnt += 1
                i += 3
        if cnt != 0:
            for k in range(j + 1, j + 1 + cnt):
                cards[k] += cards[j]

    print(sum(cards))