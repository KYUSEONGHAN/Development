# https://school.programmers.co.kr/learn/courses/30/lessons/120884
# programmers, level0: 치킨 쿠폰, python3
def solution(chicken: int) -> int:
    answer = 0
    coupon = chicken

    while coupon >= 10:
        eaten = coupon // 10
        answer += eaten
        coupon = coupon % 10 + eaten

    return answer

if __name__ == '__main__':
    print(solution(100))   # 11
    print(solution(1081))  # 120