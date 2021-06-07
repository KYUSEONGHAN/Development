# boj, 5622 : 다이얼, python3
# 문자열, 구현 알고리즘
convert_dial = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4, 'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6,
                'P':7, 'Q':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9, 'Z':9}

def dial(l):
    return sum([convert_dial[i] for i in l]) + len(l)

ring = list(input())

print(dial(ring))