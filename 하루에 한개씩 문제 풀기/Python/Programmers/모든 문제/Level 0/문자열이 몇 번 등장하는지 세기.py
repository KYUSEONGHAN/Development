def solution(myString: str, pat: str) -> int:
    result = 0

    for x in range(len(myString) - len(pat) + 1):
        if myString[x:x + len(pat)] == pat:
            result += 1

    return result