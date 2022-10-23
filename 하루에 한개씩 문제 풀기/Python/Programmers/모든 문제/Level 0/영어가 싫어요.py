# https://school.programmers.co.kr/learn/courses/30/lessons/120894
# programmers, level0: 영어가 싫어요, python3
def solution(numbers: str) -> int:
    return int(numbers.replace("one", "1").replace("two", "2").replace("three", "3").replace("four", "4").replace("five", "5").replace("six", "6").replace("seven", "7").replace("eight", "8").replace("nine", "9").replace("zero", "0"))


if __name__ == '__main__':
    print(solution("onetwothreefourfivesixseveneightnine"))  # 123456789
    print(solution("onefourzerosixseven"))  # 14067