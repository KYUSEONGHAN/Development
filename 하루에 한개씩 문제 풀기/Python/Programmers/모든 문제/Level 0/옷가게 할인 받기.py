# https://school.programmers.co.kr/learn/courses/30/lessons/120818
# programemrs, level0: 옷가게 할인 받기, python3
def solution(price: int) -> int:
    if price >= 500000:
        return int(price * 0.8)
    if price >= 300000:
        return int(price * 0.9)
    if price >= 100000:
        return int(price * 0.95)
    return price

if __name__ == '__main__':
    print(solution(150000))  # 142,500
    print(solution(580000))  # 464,000