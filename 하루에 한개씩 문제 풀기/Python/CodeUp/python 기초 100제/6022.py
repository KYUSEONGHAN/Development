yymmdd = str(input())
result = []
cnt = 0

for _ in range(3):
    result.append(yymmdd[cnt:cnt+2])
    cnt += 2

print(" ".join(result))