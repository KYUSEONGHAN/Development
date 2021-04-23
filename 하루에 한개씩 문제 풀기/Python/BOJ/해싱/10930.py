# boj, 10930 : SHA-256, python3
from hashlib import sha256

S = str(input())

print(sha256(S.encode()).hexdigest())