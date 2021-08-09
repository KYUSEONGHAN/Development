# HackerRank, Finding the percentage, python3
def solve(query, student):
    return sum(student[query]) / len(student[query])


if __name__ == '__main__':
    n = int(input())

    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    print("{:.2f}".format(solve(query_name, student_marks)))