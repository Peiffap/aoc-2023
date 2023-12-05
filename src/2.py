part = 2

f = open("../data/2.txt", "r")
sum = 0

for i, l in enumerate(f):
    def find_highest(s, highest):
        if s[0] == ':':
            return highest
        elif s[:4] == 'der ':
            for i in range(5, len(s)):
                if not s[i].isdigit():
                    highest[0] = max(highest[0], int(s[4:i][::-1]))
                    return find_highest(s[i-1:], highest)
        elif s[:6] == 'neerg ':
            for i in range(7, len(s)):
                if not s[i].isdigit():
                    highest[1] = max(highest[1], int(s[6:i][::-1]))
                    return find_highest(s[i-1:], highest)
        elif s[:5] == 'eulb ':
            for i in range(6, len(s)):
                if not s[i].isdigit():
                    highest[2] = max(highest[2], int(s[5:i][::-1]))
                    return find_highest(s[i-1:], highest)
        else:
            return find_highest(s[1:], highest)

    h = find_highest(l[::-1], [0, 0, 0])
    if part == 1:
        if h[0] <= 12 and h[1] <= 13 and h[2] <= 14:
            sum += i + 1
    if part == 2:
        sum += h[0] * h[1] * h[2]

print(sum)
f.close()