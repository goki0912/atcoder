from math import gcd
A, B, C = map(int, input().split())
gcd = gcd(gcd(A, B), C)
print(A//gcd + B//gcd + C//gcd - 3)