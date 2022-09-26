# https://www.acmicpc.net/problem/1620
# boj, 1620: 나는야 포켓몬 마스터 이다솜, python3
def solve(dict_poketmons: dict, list_poketmons: list, hit: str) -> str:
    return list_poketmons[int(hit)-1] if hit.isdigit() else dict_poketmons[hit]

if __name__ == '__main__':
    n, m = map(int, input().split())  # n: 도감에 수록되있는 포켓몬 개수, m: 맞춰야 하는 문제의 수
    dict_poketmons, list_poketmons = {}, []

    for index in range(1, n+1):
        poketmon = str(input())

        dict_poketmons[poketmon] = index
        list_poketmons.append(poketmon)

    for _ in range(m):
        hit = str(input())

        print(solve(dict_poketmons, list_poketmons, hit))