# programmers, phase2 : 전화번호 목록, python3
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for x, y in zip(phoneBook, phoneBook[1:]):
        if y.startswith(x):
            return False
    return True