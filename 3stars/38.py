A, B = map(int, input().split())
a = max(A, B)
b = min(A, B)

while b != 0:
  a,b = b, a % b

lcm = A*B // a
if lcm > 10**18:
  print("Large")
else:
  print(lcm)

