# boj, 10809 : 알파벳 찾기, python3
S = str(input())
alpabet = [chr(i) for i in range(97,122+1)]

for i in alpabet:
    try:
        print(S.index(i), end= ' ')
    except:
        print(-1, end = ' ')