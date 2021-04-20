word = ord(str(input()))

result = [chr(i) for i in range(97,word+1)]

print(" ".join(result))