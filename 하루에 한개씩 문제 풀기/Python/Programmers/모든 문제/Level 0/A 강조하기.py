def solution(myString: str) -> str:
    return ''.join(map(str, ['A' if x.lower() == 'a' else x.lower() for x in myString]))