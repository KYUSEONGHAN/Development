# https://www.acmicpc.net/problem/25501
# boj, 25501: 재귀의 귀재, python3
def recursion(s: str, l: int, r: int, cnt: int):
    cnt += 1
    if l >= r:
        return 1, cnt
    elif s[l] != s[r]:
        return 0, cnt
    return recursion(s, l+1, r-1, cnt)

def isPalindrome(s: str, cnt: int):
    return recursion(s, 0, len(s)-1, cnt)

if __name__ == '__main__':
    t = int(input())  # 테스트케이스의 개수

    for _ in range(t):
        s = str(input())  # 문자열 s
        cnt = 0           # recursion 호출 횟수
        print(*isPalindrome(s, cnt))
