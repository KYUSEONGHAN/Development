def solution(ineq: str, eq: str, n: int, m: int) -> int:
    if ineq == "<":
        if eq == "=":
            return int(n <= m)
        elif eq == "!":
            return int(n < m)
    elif ineq == ">":
        if eq == "=":
            return int(n >= m)
        elif eq == "!":
            return int(n > m)