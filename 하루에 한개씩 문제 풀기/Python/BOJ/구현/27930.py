# https://www.acmicpc.net/problem/27930
# boj, 27930: 당신은 운명을 믿나요?, python3
def solve(s: str) -> str:
    korea = {'K': 0, 'O': 0, 'R': 0, 'E': 0, 'A': 0}
    yonsei = {'Y': 0, 'O': 0, 'N': 0, 'S': 0, 'E': 0, 'I': 0}

    for x in s:
        if all(value > 0 for value in korea.values()):
            return 'KOREA'
        if all(value > 0 for value in yonsei.values()):
            return 'YONSEI'
        if x in ['K', 'O', 'R', 'E', 'A']:
            korea[x] += 1
        if x in ['Y', 'O', 'N', 'S', 'E', 'I']:
            yonsei[x] += 1

if __name__ == '__main__':
    s = str(input())

    print(solve(s))