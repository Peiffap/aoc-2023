from collections import defaultdict
import heapq

fo = open("../data/17.txt", "r")
f = list(fo)
fo.close()

grid = []
for l in f:
    grid.append([int(i) for i in l.strip()])

seen = defaultdict(lambda: 4)

q = [(0, 0, 0, 0, (0, 1), [(0, 0)])] # total cost, row, col, #consec, direction
m = 0
while q:
    node = heapq.heappop(q)
    if node[0] > m:
        #print(node[0])
        m = node[0]
    if 0 <= node[1] < len(grid[0]) and 0 <= node[2] < len(grid) and node[3] < seen[node[1], node[2], node[4]]:
        if node[1] == len(grid[0]) - 1 and node[2] == len(grid) - 1:
            print(node[0])
            break
        cnt = 0
        path = []
        for nsteps in range(1, 3 + 1 - node[3]):
            nrow = node[1] + nsteps * node[4][0]
            ncol = node[2] + nsteps * node[4][1]
            if 0 <= nrow < len(grid[0]) and 0 <= ncol < len(grid):
                cnt += grid[nrow][ncol]
                path.append((nrow, ncol))
                heapq.heappush(q, (node[0] + cnt, nrow, ncol, node[3] + nsteps, node[4], node[5] + path.copy()))
            else:
                break
        if node[4] == (1, 0) or node[4] == (-1, 0):
            for ndir in [(0, 1), (0, -1)]:
                cnt = 0
                path = []
                for nsteps in range(1, 3 + 1):
                    nrow = node[1] + nsteps * ndir[0]
                    ncol = node[2] + nsteps * ndir[1]
                    if 0 <= nrow < len(grid[0]) and 0 <= ncol < len(grid):
                        cnt += grid[nrow][ncol]
                        path.append((nrow, ncol))
                        heapq.heappush(q, (node[0] + cnt, nrow, ncol, nsteps, ndir, node[5] + path.copy()))
                    else:
                        break
        elif node[4] == (0, 1) or node[4] == (0, -1):
            for ndir in [(1, 0), (-1, 0)]:
                cnt = 0
                path = []
                for nsteps in range(1, 3 + 1):
                    nrow = node[1] + nsteps * ndir[0]
                    ncol = node[2] + nsteps * ndir[1]
                    if 0 <= nrow < len(grid[0]) and 0 <= ncol < len(grid):
                        cnt += grid[nrow][ncol]
                        path.append((nrow, ncol))
                        heapq.heappush(q, (node[0] + cnt, nrow, ncol, nsteps, ndir, node[5] + path.copy()))
                    else:
                        break
        seen[(node[1], node[2], node[4])] = node[3]

def mmin(s):
    if len(s) == 0:
        return 11
    return min(s)

def mmax(s):
    if len(s) == 0:
        return -1
    return max(s)

seen = defaultdict(set)

q = [(0, 0, 0, 0, (0, 1)), (0, 0, 0, 0, (1, 0))] # total cost, row, col, #consec, direction
m = 0
while q:
    node = heapq.heappop(q)
    if node[0] > m:
        #print(node[0])
        m = node[0]
    if 0 <= node[1] < len(grid[0]) and 0 <= node[2] < len(grid) and (node[3] < 4 and mmin(seen[node[1], node[2], node[4]]) > node[3] or node[3] >= 4 and mmax(seen[node[1], node[2], node[4]]) < 4):
        if node[1] == len(grid[0]) - 1 and node[2] == len(grid) - 1 and node[3] >= 4:
            print(node[0])
            break
        cnt = 0
        if node[3] == 0:
            for nsteps in range(1, 10 + 1):
                nrow = node[1] + nsteps * node[4][0]
                ncol = node[2] + nsteps * node[4][1]
                if 0 <= nrow < len(grid[0]) and 0 <= ncol < len(grid):
                    cnt += grid[nrow][ncol]
                    if nsteps >= 4:
                        heapq.heappush(q, (node[0] + cnt, nrow, ncol, nsteps, node[4]))
                else:
                    break
        if node[3] >= 4 and (node[4] == (1, 0) or node[4] == (-1, 0)):
            for ndir in [(0, 1), (0, -1)]:
                heapq.heappush(q, (node[0], node[1], node[2], 0, ndir))
        elif node[3] >= 4 and (node[4] == (0, 1) or node[4] == (0, -1)):
            for ndir in [(1, 0), (-1, 0)]:
                heapq.heappush(q, (node[0], node[1], node[2], 0, ndir))
        seen[(node[1], node[2], node[4])].add(node[3])