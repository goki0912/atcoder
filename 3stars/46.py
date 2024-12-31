N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
count = 0
a, b, c = [0] * 46, [0] * 46, [0] * 46
for i in range(N):
  a[A[i] % 46] += 1
  b[B[i] % 46] += 1
  c[C[i] % 46] += 1

for i in range(46):
  for j in range(46):
    for k in range(46):
      if (i+j+k) % 46 == 0:
        count += a[i] * b[j] * c[k]

print(count)