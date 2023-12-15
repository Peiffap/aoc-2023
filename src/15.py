fo = open("../data/15.txt", "r")
f = list(fo)
fo.close()

total = 0
f = f[0].strip().split(',')
for s in f:
    cv = 0
    for c in s:
        cv += ord(c)
        cv *= 17
        cv %= 256
    total += cv

print(total)

total = 0
boxes = []
for i in range(256):
    boxes.append([])
for s in f:
    cv = 0
    for i, c in enumerate(s):
        if c.isalpha():
            cv += ord(c)
            cv *= 17
            cv %= 256
        elif c == '-':
            for j, b in enumerate(boxes[cv]):
                if s[:i] == b[0]:
                    boxes[cv] = boxes[cv][:j] + boxes[cv][j + 1:]
                    break
            break
        elif c == '=':
            if boxes[cv]:
                for j, b in enumerate(boxes[cv]):
                    if s[:i] == b[0]:
                        boxes[cv][j][1] = int(s[i + 1:])
                        break
                    elif j == len(boxes[cv]) - 1:
                        boxes[cv].append([s[:i], int(s[i + 1:])])
            else:
                boxes[cv].append([s[:i], int(s[i + 1:])])
            break

for i, box in enumerate(boxes, 1):
    if box:
        for j, l in enumerate(box, 1):
            total += i * j * l[1]

print(total)

