part = 2

fo = open("../data/7.txt", "r")
f = list(fo)
fo.close()

if part == 1:
    def prep(s):
        cnts = []
        for i, c in enumerate(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']):
            cnts.append([s.count(c), c])
        
        cnts.sort(reverse=True)

        nfi = 0
        nfo = 0
        nth = 0
        ntw = 0
        no = 0

        for cnt, c in cnts:
            if cnt == 5:
                nfi += 1
            elif cnt == 4:
                nfo += 1
            elif cnt == 3:
                nth += 1
            elif cnt == 2:
                ntw += 1
            elif cnt == 1:
                no += 1

        ns = str(nfi) + str(nfo) + str(nth) + str(ntw) + str(no)

        return ns + s

    def repl(s):
        s = s.replace('A', 'M')
        s = s.replace('K', 'L')
        s = s.replace('Q', 'K')
        s = s.replace('J', 'J')
        s = s.replace('T', 'I')
        s = s.replace('9', 'H')
        s = s.replace('8', 'G')
        s = s.replace('7', 'F')
        s = s.replace('6', 'E')
        s = s.replace('5', 'D')
        s = s.replace('4', 'C')
        s = s.replace('3', 'B')
        s = s.replace('2', 'A')
        return s
elif part == 2:
    def prep(s):
        cnts = []
        for i, c in enumerate(['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M']):
            cnts.append([s.count(c), c])
        
        cnts.sort(reverse=True)
        cnts[0][0] += s.count('A')

        nfi = 0
        nfo = 0
        nth = 0
        ntw = 0
        no = 0

        for cnt, c in cnts:
            if cnt == 5:
                nfi += 1
            elif cnt == 4:
                nfo += 1
            elif cnt == 3:
                nth += 1
            elif cnt == 2:
                ntw += 1
            elif cnt == 1:
                no += 1

        ns = str(nfi) + str(nfo) + str(nth) + str(ntw) + str(no)

        return ns + s

    def repl(s):
        s = s.replace('A', 'M')
        s = s.replace('K', 'L')
        s = s.replace('Q', 'K')
        s = s.replace('J', 'A')
        s = s.replace('T', 'J')
        s = s.replace('9', 'I')
        s = s.replace('8', 'H')
        s = s.replace('7', 'G')
        s = s.replace('6', 'F')
        s = s.replace('5', 'E')
        s = s.replace('4', 'D')
        s = s.replace('3', 'C')
        s = s.replace('2', 'B')
        return s

hands = []

for l in f:
    hand, bid = l.strip().split()
    hand = repl(hand)
    bid = int(bid)
    hand = prep(hand)
    hands.append((hand, bid))
hands.sort(key=lambda h: h[0])
s = 0
for i, t in enumerate(hands, 1):
    h, b = t
    s += b * i
print(s)