def array_universe(fileinput):
    f = open("2025CGW Task 2 Input.txt", "r")
    readline = f.readlines()

    N, M = map(int, readline[0].split())
    universe = [list(map(int, line.split())) for line in readline[1:]]

    return N, M, universe

def array_offsets(i, j, N, M):
    #16 neighbour numbers
    offset_nums = [(-2,-2), (-2,-1), (-2,0), (-2,1), (-2, 2),
               (-1,2), (-1,-1), (-1,0), (-1,1), (-1, 2),
               (0,-2), (0, -1), (0,1), (0,2), (1,-2),
               (1,-1), (1,0), (1, 1), (1, 2), (2, -2),
               (2, -1), (2,0), (2,1), (2,2)]
    return [((i+di) % N, (j+dj) % M) for di, dj in offset_nums]

def grav_centers(universe, N, M):
    centers=[]

    for i in range(N):
        for j in range(M):
            neighbour_nums = array_offsets(i, j, N, M)
            if all(universe[i][j] > universe[ni][nj] for ni, nj in neighbour_nums):
                centers.append((i,j))
    return centers

def stability(universe, i, j, N, M):
    axis = [((-1,0), (1,0)), ((0,-1), (0,1)), ((-1,-1), (1,1)), ((-1,1), (1,-1))]

    for(d1,d2) in axis:
        ni1, nj1 = (i+d1[0]) % N, (j+d1[1]) % M
        ni2, nj2 = (i+d2[0]) % N, (j+d2[1]) % M

        if universe[ni1][nj1] != universe[ni2][nj2]:
            return False
    return True

def stable_unstable(universe, centers, N, M):
    stable = 0
    unstable = 0

    for i, j in centers:
        if stability(universe, i, j, N, M):
            stable += 1
        else:
            unstable += 1
    return stable, unstable

#main
N, M, universe = array_universe("2025CGW Task 2 Input.txt")
centers = grav_centers(universe, N, M)
stable, unstable = stable_unstable(universe, centers, N, M)

print(stable, unstable)
    
