def sudo_money(P: int, Q: int, R: int, S: int, W: int) -> int:
    a_company = W * P
    b_company = Q + (W - R) * S if W > R else Q

    return min(a_company, b_company)


T = int(input())

for test_case in range(1, T + 1):
    P, Q, R, S, W = map(int, input().split())
    print(f'#{test_case} {sudo_money(P, Q, R, S, W)}')