def solution(myString: str, pat: str) -> int:
    myString, pat = myString.lower(), pat.lower()

    return 1 if pat in myString else 0