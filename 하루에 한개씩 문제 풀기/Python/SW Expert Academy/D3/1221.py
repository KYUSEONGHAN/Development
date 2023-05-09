from typing import List

def GNS(data: List[str]) -> List[str]:
    dict = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    return sorted(data, key=lambda x: dict[x])

T = int(input())

for _ in range(1, T + 1):
    test_case, test_case_len = input().split()
    data = list(map(str, input().split()))
    print(test_case)
    print(*GNS(data))