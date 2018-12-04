'''
Given a N by M matrix of numbers, print out the matrix in a clockwise spiral.

For example, given the following matrix:

    [[1,  2,  3,  4,  5],   <-- matrix[0]
    [6,  7,  8,  9,  10],   <-- matrix[1]
    [11, 12, 13, 14, 15],   <-- matrix[2]
    [16, 17, 18, 19, 20]]   <-- matrix[3]

You should print out the following:

1
2
3
4
5
10
15
20
19
18
17
16
11
6
7
8
9
14
13
12

'''

def spiral(m):
    Xmin = 0
    minY = 0
    Xmax = len(m)-1
    maxY = len(m[0])-1
    size = len(m) * len(m[0])
    # print(size)
    count = 0

    while size > 0:
        for i in range(minY, maxY+1, 1):
            size -= 1
            # print(m[Xmin][i], size)
            print(m[Xmin][i])
            if size == 0:
                return

        for i in range(Xmin+1, Xmax+1, 1):
            size -= 1
            # print(m[i][maxY], size)
            print(m[i][maxY])
            if size == 0:
                return

        for i in range(maxY-1, minY-1, -1):
            size -= 1
            # print(m[Xmax][i], size)
            print(m[Xmax][i])
            if size == 0:
                return

        for i in range(Xmax-1, Xmin, -1):
            size -= 1
            # print(m[i][minY], size)
            print(m[i][minY])
            if size == 0:
                return

        Xmin += 1
        minY += 1
        Xmax -= 1
        maxY -=1



matrix = [
    [1,  2,  3,  4,  5],
    [6,  7,  8,  9,  10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],
    [26, 27, 28, 29, 30],
    [31, 32, 33, 34, 35],
    [36, 37, 38, 39, 40]
    ]

spiral(matrix)
