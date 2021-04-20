import sys

h, w = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
grid = [[0 for j in range(w)] for i in range(h)]
makdae = []
cnt = 0
len_num = 1

for _ in range(n):
    makdae_info = list(map(int, sys.stdin.readline().split()))
    makdae.append(makdae_info)
#     길이, (0 = 세로, 1 = 가로), x_point, y_point

for i in makdae:
    grid[i[2] - 1][i[3] - 1] += 1
    if i[1] == 0:
        for _ in range(i[0] - 1):
            grid[i[2] - 1][i[3] - 1 + len_num] += 1
            len_num += 1
        len_num = 1
    else:
        for _ in range(i[0] - 1):
            grid[i[2] - 1 + len_num][i[3] - 1] += 1
            len_num += 1
        len_num = 1

for _ in range(h):
    print(" ".join(map(str, grid[cnt])))
    cnt += 1