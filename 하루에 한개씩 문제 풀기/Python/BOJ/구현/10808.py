# boj, 10808: 알파뱃 개수, python3
def solve(word):
    alpa = {chr(x):0 for x in range(97, 122+1)}

    for x in word:
        if x in alpa:
            alpa[x] = alpa[x] +1

    for x in alpa:
        print(alpa[x], end=' ')

if __name__ == '__main__':
    s = str(input())  # baekjoon

    solve(s)