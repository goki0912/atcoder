N, Q = map(int, input().split())
A = list(map(int, input().split()))
shifts = 0

for i in range(Q):
  T, x, y = map(int, input().split())
  if T == 1:
    A[((x-1)-shifts) % N], A[((y-1)-shifts) % N] = A[((y-1)-shifts) % N], A[((x-1)-shifts) % N]
  elif T == 2:
    shifts = (shifts+1) % N
  elif T == 3:
    print(A[(x-1-shifts) % N])