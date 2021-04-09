# boj, 7568 : 덩치, python3
N = int(input())

if N > 51 or N < 2:
    print("N range error")
else:
    weight = []
    height = []
    rank = 0
    s = []
    answer = []

    for i in range(N):
        w, h = list(map(int,input().split()))
        if w > 200 or w < 10:
            print("w range error")
            break
        elif h > 200 or h < 10:
            print("h range error")
            break
        else:
            weight.append(w)
            height.append(h)

    deongchi = [list(a) for a in zip(weight,height)]     #zip type convert tuple -> list

    for i in range(N):
        deongchi[i].append(i)    #add index

    w_sort = sorted(deongchi, key = lambda x : x[0])

    for i in range(N):
        weight,height = w_sort[i][0],w_sort[i][1]
        rank = 1
        for j in range(i+1,N):
            if height < w_sort[j][1] and weight < w_sort[j][0] :
                rank += 1
        s.append((w_sort[i][2],rank))

    s.sort()

    for i in range(N):
        answer.append(s[i][1])

    for i in range (0, N):
        print(answer[i], end = ' ')