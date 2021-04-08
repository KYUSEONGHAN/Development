# boj, 9012 : 괄호, Python3
T = int(input())
ps = []
result = 0

for _ in range(T):
    ps.append(input().split())

for i in range(len(ps)):
    for j in range(len(ps[i])):
        result += ps[i][j].count("(")
        result -= ps[i][j].count(")")
        if result == 0:
            print('YES')
        else:
            print('NO')
        result = 0

# 수정 후 코드
T = int(input())

for i in range(T):
    ps = list(input())

    while len(ps) != 0:
        if ps[0] == ')':
            print('NO')
            break
        else:
            if ')' in ps:
                ps.remove(')')
                ps.remove('(')
            else:
                print("NO")
                break
    if len(ps) == 0:
        print("YES")