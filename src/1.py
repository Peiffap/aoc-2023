part = 2

f = open("../data/1.txt", "r")
sum = 0

if part == 1:
    def find_first_only_number(s):
        for c in s:
            if c.isdigit():
                return int(c)

    for s in f:
        sum += 10 * find_first_only_number(s) + find_first_only_number(s[::-1])
elif part == 2:
    def find_first(s):
        if s[0].isdigit():
            return int(s[0])
        elif s[:3] == 'one':
            return 1
        elif s[:3] == 'two':
            return 2
        elif s[:5] == 'three':
            return 3
        elif s[:4] == 'four':
            return 4
        elif s[:4] == 'five':
            return 5
        elif s[:3] == 'six':
            return 6
        elif s[:5] == 'seven':
            return 7
        elif s[:5] == 'eight':
            return 8
        elif s[:4] == 'nine':
            return 9
        else:
            return find_first(s[1:])

    def find_first_reverse(s):
        if s[0].isdigit():
            return int(s[0])
        elif s[:3] == 'eno':
            return 1
        elif s[:3] == 'owt':
            return 2
        elif s[:5] == 'eerht':
            return 3
        elif s[:4] == 'ruof':
            return 4
        elif s[:4] == 'evif':
            return 5
        elif s[:3] == 'xis':
            return 6
        elif s[:5] == 'neves':
            return 7
        elif s[:5] == 'thgie':
            return 8
        elif s[:4] == 'enin':
            return 9
        else:
            return find_first_reverse(s[1:])

    for s in f:
        sum += 10 * find_first(s) + find_first_reverse(s[::-1])

print(sum)
f.close()