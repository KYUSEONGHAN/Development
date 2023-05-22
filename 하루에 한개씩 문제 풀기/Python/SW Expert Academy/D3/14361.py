from itertools import permutations

t = int(input())

for tc in range(1, t + 1):
    n = input()
    num = int(n)
    length = len(n)
    num_list = []
    check = 0

    if len(n) == 1:
        print('#%d impossible' % tc)
        continue

    for i in permutations(n, length):
        temp = ''
        for j in i:
            temp += j
        if temp[0] != '0':
            if int(temp) not in num_list:
                num_list.append(int(temp))

    for i in range(1, len(num_list)):
        if num_list[i] % num_list[0] == 0:
            check = 1

    if check == 1:
        print('#%d possible' % tc)
    else:
        print('#%d impossible' % tc)