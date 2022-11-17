# https://school.programmers.co.kr/learn/courses/30/lessons/120869
# programmers, level0: 외계어 사전, python3
def solution(spell: list, dic: list):
    spell = {i: 0 for i in spell}

    for x in dic:
        if len(x) == len(spell):
            for y in x:
                if y in spell:
                    spell[y] += 1
                else:
                    break
            if len(set(spell.values())) == 1 and sum(set(spell.values())) == 1:
                return 1
            spell = {i: 0 for i in spell}

    return 2

if __name__ == '__main__':
    print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))          # 2
    print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))                 # 1
    print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))    # 2