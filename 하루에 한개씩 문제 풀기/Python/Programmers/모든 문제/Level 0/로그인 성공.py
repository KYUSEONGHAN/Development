# https://school.programmers.co.kr/learn/courses/30/lessons/120883
# programmers, level0: 로그인 성공?, python3
def solution(id_pw: list, db: list) -> str:
    for x in db:
        if id_pw == x:
            return 'login'
        elif id_pw[0] == x[0] and id_pw[1] != x[1]:
            return 'wrong pw'

    return 'fail'

if __name__ == '__main__':
    print(solution(id_pw=["meosseugi", "1234"], db=[["rardss", "123"], ["yyoom", "1234"], ["meosseugi", "1234"]]))
    print(solution(id_pw=["programmer01", "15789"], db=[["programmer02", "111111"], ["programmer00", "134"], ["programmer01", "1145"]]))
    print(solution(id_pw=["rabbit04", "98761"], db=[["jaja11", "98761"], ["krong0313", "29440"], ["rabbit00", "111333"]]))