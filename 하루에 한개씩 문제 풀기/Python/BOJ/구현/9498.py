# boj, 9498 : 시험 성적, python3
score = int(input())

if score < 0 or score > 100:
    print("score range error")
else:
    if score >= 90 and score <= 100:
        print("A")
    elif score >= 80 and score <= 89:
        print("B")
    elif score >= 70 and score <= 79:
        print("C")
    elif score >= 60 and score <= 69:
        print("D")
    else:
        print("F")