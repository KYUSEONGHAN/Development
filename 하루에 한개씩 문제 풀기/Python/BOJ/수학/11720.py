# boj, 11720 : 숫자의 합, python3
N = int(input())

if N > 100 or N < 1:
    print("N range error")
else:
    num = list(input())
    result = []

    for i in num:
        result.append(int(i))

    if len(result) != N:
        print("error")
    else:
        print(sum(result))